# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UUMF.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(875, 540)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(875, 498))
        self.centralwidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(7)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.gridLayout.addWidget(self.tableWidget, 3, 0, 1, 2)
        self.basic_data = QtWidgets.QHBoxLayout()
        self.basic_data.setObjectName("basic_data")
        self.classesLabel = QtWidgets.QLabel(self.centralwidget)
        self.classesLabel.setObjectName("classesLabel")
        self.basic_data.addWidget(self.classesLabel)
        self.classes = QtWidgets.QLineEdit(self.centralwidget)
        self.classes.setObjectName("classes")
        self.basic_data.addWidget(self.classes)
        self.seatLabel = QtWidgets.QLabel(self.centralwidget)
        self.seatLabel.setTextFormat(QtCore.Qt.PlainText)
        self.seatLabel.setObjectName("seatLabel")
        self.basic_data.addWidget(self.seatLabel)
        self.seat = QtWidgets.QLineEdit(self.centralwidget)
        self.seat.setObjectName("seat")
        self.basic_data.addWidget(self.seat)
        self.submit = QtWidgets.QPushButton(self.centralwidget)
        self.submit.setObjectName("submit")
        self.basic_data.addWidget(self.submit)
        self.combinations = QtWidgets.QComboBox(self.centralwidget)
        self.combinations.setObjectName("combinations")
        self.basic_data.addWidget(self.combinations)
        self.gridLayout.addLayout(self.basic_data, 0, 0, 1, 2)
        self.days = QtWidgets.QHBoxLayout()
        self.days.setObjectName("days")
        self.sa = QtWidgets.QCheckBox(self.centralwidget)
        self.sa.setObjectName("sa")
        self.days.addWidget(self.sa)
        self.su = QtWidgets.QCheckBox(self.centralwidget)
        self.su.setChecked(False)
        self.su.setTristate(False)
        self.su.setObjectName("su")
        self.days.addWidget(self.su)
        self.mo = QtWidgets.QCheckBox(self.centralwidget)
        self.mo.setObjectName("mo")
        self.days.addWidget(self.mo)
        self.tu = QtWidgets.QCheckBox(self.centralwidget)
        self.tu.setObjectName("tu")
        self.days.addWidget(self.tu)
        self.we = QtWidgets.QCheckBox(self.centralwidget)
        self.we.setObjectName("we")
        self.days.addWidget(self.we)
        self.th = QtWidgets.QCheckBox(self.centralwidget)
        self.th.setObjectName("th")
        self.days.addWidget(self.th)
        self.fr = QtWidgets.QCheckBox(self.centralwidget)
        self.fr.setObjectName("fr")
        self.days.addWidget(self.fr)
        self.gridLayout.addLayout(self.days, 1, 0, 1, 1)
        self.times = QtWidgets.QHBoxLayout()
        self.times.setObjectName("times")
        self.slot1 = QtWidgets.QCheckBox(self.centralwidget)
        self.slot1.setObjectName("slot1")
        self.times.addWidget(self.slot1)
        self.slot2 = QtWidgets.QCheckBox(self.centralwidget)
        self.slot2.setObjectName("slot2")
        self.times.addWidget(self.slot2)
        self.slot3 = QtWidgets.QCheckBox(self.centralwidget)
        self.slot3.setObjectName("slot3")
        self.times.addWidget(self.slot3)
        self.slot4 = QtWidgets.QCheckBox(self.centralwidget)
        self.slot4.setObjectName("slot4")
        self.times.addWidget(self.slot4)
        self.slot5 = QtWidgets.QCheckBox(self.centralwidget)
        self.slot5.setObjectName("slot5")
        self.times.addWidget(self.slot5)
        self.slot6 = QtWidgets.QCheckBox(self.centralwidget)
        self.slot6.setObjectName("slot6")
        self.times.addWidget(self.slot6)
        self.slot7 = QtWidgets.QCheckBox(self.centralwidget)
        self.slot7.setObjectName("slot7")
        self.times.addWidget(self.slot7)
        self.gridLayout.addLayout(self.times, 2, 0, 1, 1)
        self.status = QtWidgets.QVBoxLayout()
        self.status.setObjectName("status")
        self.statusLabel = QtWidgets.QLabel(self.centralwidget)
        self.statusLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.statusLabel.setObjectName("statusLabel")
        self.status.addWidget(self.statusLabel)
        self.statusLine = QtWidgets.QLineEdit(self.centralwidget)
        self.statusLine.setReadOnly(True)
        self.statusLine.setObjectName("statusLine")
        self.status.addWidget(self.statusLine)
        self.gridLayout.addLayout(self.status, 1, 1, 2, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ultimate Usis Mother Father"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "08.00 AM"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "09.30 AM"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "11.00 AM"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "12.30 PM"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "02.00 PM"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "03.30 PM"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "05.00 PM"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Saturday"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Sunday"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Monday"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Tuesday"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Wednesday"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Thursday"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Friday"))
        self.classesLabel.setText(_translate("MainWindow", "Classes"))
        self.seatLabel.setText(_translate("MainWindow", "Seats"))
        self.submit.setText(_translate("MainWindow", "Submit"))
        self.sa.setText(_translate("MainWindow", "Saturday"))
        self.su.setText(_translate("MainWindow", "Sunday"))
        self.mo.setText(_translate("MainWindow", "Monday"))
        self.tu.setText(_translate("MainWindow", "Tuesday"))
        self.we.setText(_translate("MainWindow", "Wednesday"))
        self.th.setText(_translate("MainWindow", "Thursday"))
        self.fr.setText(_translate("MainWindow", "Friday"))
        self.slot1.setText(_translate("MainWindow", "8 AM"))
        self.slot2.setText(_translate("MainWindow", "9.3 AM"))
        self.slot3.setText(_translate("MainWindow", "11 AM"))
        self.slot4.setText(_translate("MainWindow", "12.3 PM"))
        self.slot5.setText(_translate("MainWindow", "2 PM"))
        self.slot6.setText(_translate("MainWindow", "3.3 PM"))
        self.slot7.setText(_translate("MainWindow", "5 PM"))
        self.statusLabel.setText(_translate("MainWindow", "Status"))
