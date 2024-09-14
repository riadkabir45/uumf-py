from requests import Session as Curl
from re import search as RegSearch
from re import findall as RegSearchAll
from itertools import product as Posibility
from json import loads as Jload

class InvalidUsisUser(Exception):
    pass

def getCredins(credins):
	downloader = Curl()
	res = downloader.get('https://usis.bracu.ac.bd/idp/realms/interim/protocol/openid-connect/auth?client_id=frontend&redirect_uri=https%3A%2F%2Fusis.bracu.ac.bd%2Finterim%2F&response_mode=fragment&response_type=code&scope=openid')
	res = downloader.post('https://usis.bracu.ac.bd/idp/realms/interim/login-actions/authenticate?'+RegSearch('session_code[^"]+',str(res.content)).group().replace("&amp;", "&"),data=credins)
	res = downloader.post('https://usis.bracu.ac.bd/idp/realms/interim/protocol/openid-connect/token',data={'code':res.url.split("=")[-1],'grant_type':'authorization_code','client_id':'frontend','redirect_uri':'https://usis.bracu.ac.bd/interim/'})
	auth = res.text.split(",")[0].split(":")[1].strip('"')
	downloader.headers.update({'Authorization': 'Bearer '+auth})
	return downloader


def getCredentials(credins):
    user,passwd = credins['username'],credins['password']
    dataDownloader = Curl()
    dataDownloader.get("https://usis.bracu.ac.bd/academia")
    response = dataDownloader.post(
        "https://usis.bracu.ac.bd/academia/j_spring_security_check",
        data={"j_username": user, "j_password": passwd},
    )
    if (
        response.url
        == "https://usis.bracu.ac.bd/academia/login/authfail?login_error=1"
    ):
        raise InvalidUsisUser
    return dataDownloader


def cleanTime(times):
    timeArray = RegSearchAll('[A-Z][a-z]+\([^\)]+\)',times)
    for i in range(len(timeArray)):
        room = RegSearch('[0-9A-Z]+-[0-9A-Z]+\)|[0-9A-Za-z_]+\)',timeArray[i]).group()
        day = RegSearch('[A-Z][a-z]+',timeArray[i]).group()
        timeArray[i] = timeArray[i].replace(day,day[:2])
        timeArray[i] = timeArray[i].replace(room,"")
        timeArray[i] = timeArray[i].replace("(08:00 AM-09:20 AM-","Slot1")
        timeArray[i] = timeArray[i].replace("(09:30 AM-10:50 AM-","Slot2")
        timeArray[i] = timeArray[i].replace("(11:00 AM-12:20 PM-","Slot3")
        timeArray[i] = timeArray[i].replace("(12:30 PM-01:50 PM-","Slot4")
        timeArray[i] = timeArray[i].replace("(02:00 PM-03:20 PM-","Slot5")
        timeArray[i] = timeArray[i].replace("(03:30 PM-04:50 PM-","Slot6")
        timeArray[i] = timeArray[i].replace("(05:00 PM-06:20 PM-","Slot7")
    return timeArray


def getData(credins):
    downloader = getCredins(credins)
    response = downloader.get("https://usis.bracu.ac.bd/interim/api/v1/offered-courses")
    if '[200]' not in str(response):
        return ["EXPIRED"]
    dataTable = Jload(response.text)
    sessionId = dataTable[0]['academicSessionId']
    rex = downloader.get("https://usis.bracu.ac.bd/interim/api/v1/exam-schedules")

    usisData = {}
    for course in rex.json():
        if course['courseCode'] not in usisData:
            usisData[course['courseCode']] = {}
        usisData[course['courseCode']][course['section'][-3:-1]] = f"{course['courseCode']} - {course['examDate']} @ {course['startTime']} - {course['endTime']}"
    
    cleanedTable = []
    for data in dataTable:
        dataDict = {}
        className = data['courseCode']
        section = data['courseDetails'][-3:-1]
        fac = data['empShortName']
        seats = data['defaultSeatCapacity'] - data['totalFillupSeat']
        time = data['classSchedule']+data['classLabSchedule']
        exams = data['dayNo']
        dataDict["Class"] = className
        dataDict["Section"] = section
        dataDict["Time"] = list(map(str.upper,cleanTime(time)))
        dataDict["Seats"] = 0 if seats == None else int(seats)
        dataDict["Faculty"] = fac
        dataDict['exam'] = exams
        
        ex_course = usisData.get(className)
        if ex_course is not None:
            ex_section = ex_course.get(section)
            if ex_section is not None:
                dataDict['exam'] = ex_section
        cleanedTable.append(dataDict)
    return cleanedTable


def posibilityClasses(data,timeTable,seatv,output,time=[],secs=[]):
    if len(data) == 0:
        output.append(secs)
        return
    otime = time[:]
    osecs = secs[:]
    for classes in data[0]:
        time = otime[:]
        secs = osecs[:]
        ok = True
        for classTime in classes["Time"]:
            if classTime in time or classTime not in timeTable:
                ok = False
                break
        if not ok or classes["Seats"] < seatv:
            continue
        time.extend(classes["Time"])
        secs.append(classes)
        posibilityClasses(data[1:],timeTable,seatv,output,time,secs)

def slotter(data):
    return data[0]+"SLOT"+data[1]

def advisor(allClass,seatNumbers,strDays,strTimes,credins):
    timeTable = list(map(slotter,Posibility(strDays.upper().split(),strTimes.upper().split())))
    bigData = getData(credins)
    argv = allClass.split()

    allAdvisings = []
    for i in range(len(argv)):
        allAdvisings.append([])

    argv = list(map(str.upper,argv))

    for i in range(len(argv)):
        if '-' not in argv[i]:
            for course in bigData:
                if argv[i] == course["Class"]:
                    allAdvisings[i].append(course)
        else:
            code,sub = argv[i].split('-')
            if sub.isnumeric():
                for course in bigData:
                    if code == course["Class"] and int(sub) == int(course["Section"]):
                        allAdvisings[i].append(course)
            else:
                for course in bigData:
                    if code == course["Class"] and sub == course["Faculty"]:
                        allAdvisings[i].append(course)
    advisedClasses = []
    posibilityClasses(allAdvisings,timeTable,seatNumbers,advisedClasses)
    return advisedClasses

