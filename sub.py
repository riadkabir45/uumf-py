from requests import Session as Curl
from re import search as RegSearch
from re import findall as RegSearchAll
from itertools import product as Posibility

downloader = Curl()

def cleanTime(times):
    timeArray = RegSearchAll('[A-Z][a-z]\([^\)]+\)',times)
    for i in range(len(timeArray)):
        room = RegSearch('UB[0-9]+\)',timeArray[i]).group()
        timeArray[i] = timeArray[i].replace(room,"")
        timeArray[i] = timeArray[i].replace("(08:00 AM-09:20 AM-","Slot1")
        timeArray[i] = timeArray[i].replace("(09:30 AM-10:50 AM-","Slot2")
        timeArray[i] = timeArray[i].replace("(11:00 AM-12:20 PM-","Slot3")
        timeArray[i] = timeArray[i].replace("(12:30 PM-01:50 PM-","Slot4")
        timeArray[i] = timeArray[i].replace("(02:00 PM-03:20 PM-","Slot5")
        timeArray[i] = timeArray[i].replace("(03:30 PM-04:50 PM-","Slot6")
        timeArray[i] = timeArray[i].replace("(05:00 PM-06:20 PM-","Slot7")
    return timeArray

def getData():
    response = downloader.get("https://admissions.bracu.ac.bd/academia/admissionRequirement/getAvailableSeatStatus")
    dataTable = response.text.split("<tr>")[1:]
    cleanedTable = []
    for data in dataTable:
        dataDict = {}
        className = RegSearch('100px">[0-9A-Z]+',data).group()[7:]
        section = RegSearch('69px;">[0-9]+',data).group()[7:]
        fac = RegSearch('68px;">[A-Z]+',data).group()[7:]
        seats = RegSearch('120px;">[\-0-9]+',data).group()[8:]
        time = RegSearch('290px;">[^/]+',data).group()[8:-1]
        dataDict["Class"] = className
        dataDict["Section"] = section
        dataDict["Time"] = list(map(str.upper,cleanTime(time)))
        dataDict["Seats"] = int(seats)
        dataDict["Faculty"] = fac
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

def advisor(allClass,seatNumbers,strDays,strTimes):
    timeTable = list(map(slotter,Posibility(strDays.upper().split(),strTimes.upper().split())))
    bigData = getData()
    argv = allClass.split()

    allAdvisings = []
    for i in range(len(argv)):
        allAdvisings.append([])

    argv = list(map(str.upper,argv))

    for course in bigData:
        for i in range(len(argv)):
            if argv[i] == course["Class"]:
                allAdvisings[i].append(course)
    advisedClasses = []
    posibilityClasses(allAdvisings,timeTable,seatNumbers,advisedClasses)
    return advisedClasses

