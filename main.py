from qtui import Ui_MainWindow as MainWindow
from sub import advisor
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView, QAbstractItemView, QTableWidgetItem
from PyQt5.QtGui import QIntValidator, QStandardItem
from PyQt5.QtCore import QThread,Qt
import sys

class UUMF(MainWindow,QThread):
    def __init__(self):
        self.timeArray = []
        self.dayArray = []  
        self.bigData = []  
        
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
        
        self.classes.setText('CSE221 MaT216 cse320 cSe330')
        self.seat.setText('1')
        self.su.setChecked(True)
        self.mo.setChecked(True)
        self.tu.setChecked(True)
        self.we.setChecked(True)
        self.slot1.setChecked(True)
        self.slot2.setChecked(True)
        self.slot3.setChecked(True)
        self.slot4.setChecked(True)
        
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
    
    def handleCombo(self):
        self.tableWidget.clearContents()
        index = int(self.combinations.currentText())
        routine = self.bigData[index]
        for course in routine:
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
                self.setCell(cDayN,cSlot,f"{course['Class']} {course['Section']}\n{course['Faculty']} {course['Seats']}")
    
    def run(self):
        self.timeArray.sort()
        self.dayArray.sort()
        self.combinations.clear()
        self.combinations.update()
        self.tableWidget.clearContents()
        
        strTimes = " ".join(list(map(str,self.timeArray)))
        strDays = " ".join(self.dayArray)
        
        if self.seat.text() == "":
            self.seat.setText('1')
        
        old = self.submit.text()
        self.submit.setText("...")
        self.submit.update()
        data = advisor(self.classes.text(),int(self.seat.text()),strDays,strTimes)
        self.submit.setText(old)
        
        if len(data) != 0 and len(data[0]) != 0:
            self.combinations.addItems(list(map(str,list(range(len(data))))))
            self.bigData = data

print("riad is hacking you")
print("HAHAHAHAHAHAHAAA")
UUMF()
