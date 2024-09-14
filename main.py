from qtui import Ui_MainWindow as MainWindow
from sub import advisor
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView, QAbstractItemView, QTableWidgetItem
from PyQt5.QtGui import QIntValidator, QStandardItem
from PyQt5.QtCore import QThread,Qt
import sys
import pickle
from math import ceil



class UUMF(MainWindow,QThread):
    def __init__(self):
        self.timeArray = []
        self.dayArray = []  
        self.bigData = []

        self.fData = {}
        try:
            with open('data.pkl', 'rb') as f:
                self.fData = pickle.load(f)
        except Exception as err:
            print(err)
            self.fData['course'] = "CSE220 bIo101"
            self.fData['uname'] = ""
            self.fData['seat'] = "1"
            self.fData['sa'] = False
            self.fData['su'] = True
            self.fData['mo'] = True
            self.fData['tu'] = True
            self.fData['we'] = True
            self.fData['th'] = False
            self.fData['fr'] = False
            self.fData['slot1'] = True
            self.fData['slot2'] = True
            self.fData['slot3'] = True
            self.fData['slot4'] = True
            self.fData['slot5'] = False
            self.fData['slot6'] = False
            self.fData['slot7'] = False

        
        super().__init__()
        app = QApplication(sys.argv)
        self.win = QMainWindow()
        self.setupUi(self.win)
        
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        
        self.slot1.stateChanged.connect(lambda: self.slotClicked(1))
        self.slot2.stateChanged.connect(lambda: self.slotClicked(2))
        self.slot3.stateChanged.connect(lambda: self.slotClicked(3))
        self.slot4.stateChanged.connect(lambda: self.slotClicked(4))
        self.slot5.stateChanged.connect(lambda: self.slotClicked(5))
        self.slot6.stateChanged.connect(lambda: self.slotClicked(6))
        self.slot7.stateChanged.connect(lambda: self.slotClicked(7))
        
        self.sa.stateChanged.connect(lambda: self.dayClicked("Sa"))
        self.su.stateChanged.connect(lambda: self.dayClicked("Su"))
        self.mo.stateChanged.connect(lambda: self.dayClicked("Mo"))
        self.tu.stateChanged.connect(lambda: self.dayClicked("Tu"))
        self.we.stateChanged.connect(lambda: self.dayClicked("We"))
        self.th.stateChanged.connect(lambda: self.dayClicked("Th"))
        self.fr.stateChanged.connect(lambda: self.dayClicked("Fr"))
        
        self.combinations.currentIndexChanged.connect(self.handleCombo)
        
        self.classes.setText(self.fData['course'])
        self.seat.setText(self.fData['seat'])
        self.user.setText(self.fData['uname'])
        self.sa.setChecked(self.fData['sa'])
        self.su.setChecked(self.fData['su'])
        self.mo.setChecked(self.fData['mo'])
        self.tu.setChecked(self.fData['tu'])
        self.we.setChecked(self.fData['we'])
        self.th.setChecked(self.fData['th'])
        self.fr.setChecked(self.fData['fr'])
        self.slot1.setChecked(self.fData['slot1'])
        self.slot2.setChecked(self.fData['slot2'])
        self.slot3.setChecked(self.fData['slot3'])
        self.slot4.setChecked(self.fData['slot4'])
        self.slot5.setChecked(self.fData['slot5'])
        self.slot6.setChecked(self.fData['slot6'])
        self.slot7.setChecked(self.fData['slot7'])
        
        
        self.dynamicTextArea("No Exams Found")
        self.submit.clicked.connect(self.start)
        self.seat.setValidator(QIntValidator(0, 100))
        
        self.win.show()
        sys.exit(app.exec_())
        
    def slotClicked(self,slot):
        if slot in self.timeArray:
            self.timeArray.remove(slot)
        else:
            self.timeArray.append(slot)
    
    def dayClicked(self,day):
        if day in self.dayArray:
            self.dayArray.remove(day)
        else:
            self.dayArray.append(day)
    
    def setCell(self,x,y,text):
        item = QTableWidgetItem(text)
        item.setTextAlignment(Qt.AlignVCenter)
        item.setTextAlignment(Qt.AlignHCenter)
        self.tableWidget.setItem(y,x,item)
    
    def dynamicTextArea(self,text):
        self.examBar.setText(text)
        height = self.examBar.document().size().height()
        self.examBar.setFixedHeight(ceil(height))
    
    def handleCombo(self):
        self.tableWidget.clearContents()
        index = self.combinations.currentText()
        if not index.isdecimal():
            return
        index = int(index)
        routine = self.bigData[index]
        exams = ""
        for course in routine:
            exams += course['exam'] + '\n'
            for cTime in course["Time"]:
                cDay = cTime[:2]
                cSlot = int(cTime[-1])
                if cDay  == "SA":
                    cDayN = 0
                elif cDay  == "SU":
                    cDayN = 1
                elif cDay  == "MO":
                    cDayN = 2
                elif cDay  == "TU":
                    cDayN = 3
                elif cDay  == "WE":
                    cDayN = 4
                elif cDay  == "TH":
                    cDayN = 5
                else:
                    cDayN = 6
                self.setCell(cDayN,cSlot-1,f"{course['Class']} {course['Section']}\n{course['Faculty']} {course['Seats']}")
        self.dynamicTextArea(exams)
    
    def run(self):
        with open('data.pkl', 'wb') as f:
            self.fData['course'] = self.classes.text()
            self.fData['seat'] = self.seat.text()
            self.fData['uname'] = self.user.text()
            self.fData['sa'] = self.sa.isChecked()
            self.fData['su'] = self.su.isChecked()
            self.fData['mo'] = self.mo.isChecked()
            self.fData['tu'] = self.tu.isChecked()
            self.fData['we'] = self.we.isChecked()
            self.fData['th'] = self.th.isChecked()
            self.fData['fr'] = self.fr.isChecked()
            self.fData['slot1'] = self.slot1.isChecked()
            self.fData['slot2'] = self.slot2.isChecked()
            self.fData['slot3'] = self.slot3.isChecked()
            self.fData['slot4'] = self.slot4.isChecked()
            self.fData['slot5'] = self.slot5.isChecked()
            self.fData['slot6'] = self.slot6.isChecked()
            self.fData['slot7'] = self.slot7.isChecked()
            pickle.dump(self.fData, f)

        self.timeArray.sort()
        self.dayArray.sort()
        self.combinations.clear()
        self.combinations.update()
        self.tableWidget.clearContents()
        self.bigData.clear()
        
        strTimes = " ".join(list(map(str,self.timeArray)))
        strDays = " ".join(self.dayArray)
        
        if self.seat.text() == "":
            self.seat.setText('1')
        
        old = self.submit.text()
        self.submit.setText("...")
        self.submit.update()
        
        try:
            data = advisor(self.classes.text(),int(self.seat.text()),strDays,strTimes,credins = {'username':self.user.text(),'password':self.passwd.text()})
            self.bigData = data
        except Exception as err:
            print(str(type(err)),err)
        
        self.submit.setText(old)
        
        if len(self.bigData) != 0 and len(self.bigData[0]) != 0:
            self.combinations.addItems(list(map(str,list(range(len(self.bigData))))))

print("riad is hacking you")
print("HAHAHAHAHAHAHAAA")
UUMF()
