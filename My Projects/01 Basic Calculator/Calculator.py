#This python code performs basic mathematical operations on numbers
#Note: This calculator can only compute results upto 5 digits
#This code is created by Milan Varghese
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(403, 376)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lcddisplay = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcddisplay.setMinimumSize(QtCore.QSize(381, 111))
        self.lcddisplay.setMaximumSize(QtCore.QSize(381, 111))
        self.lcddisplay.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lcddisplay.setMidLineWidth(0)
        self.lcddisplay.setSmallDecimalPoint(False)
        self.lcddisplay.setProperty("intValue", 0)
        self.lcddisplay.setObjectName("lcddisplay")
        self.gridLayout_3.addWidget(self.lcddisplay, 0, 0, 1, 4)
        self.pb1 = QtWidgets.QPushButton(self.centralwidget)
        self.pb1.setMinimumSize(QtCore.QSize(81, 41))
        self.pb1.setMaximumSize(QtCore.QSize(90, 41))
        self.pb1.setObjectName("pb1")
        self.gridLayout_3.addWidget(self.pb1, 1, 0, 1, 1)
        self.pb2 = QtWidgets.QPushButton(self.centralwidget)
        self.pb2.setMinimumSize(QtCore.QSize(81, 41))
        self.pb2.setMaximumSize(QtCore.QSize(90, 41))
        self.pb2.setObjectName("pb2")
        self.gridLayout_3.addWidget(self.pb2, 1, 1, 1, 1)
        self.pb3 = QtWidgets.QPushButton(self.centralwidget)
        self.pb3.setMinimumSize(QtCore.QSize(81, 41))
        self.pb3.setMaximumSize(QtCore.QSize(90, 41))
        self.pb3.setObjectName("pb3")
        self.gridLayout_3.addWidget(self.pb3, 1, 2, 1, 1)
        self.pbadd = QtWidgets.QPushButton(self.centralwidget)
        self.pbadd.setMinimumSize(QtCore.QSize(81, 41))
        self.pbadd.setMaximumSize(QtCore.QSize(90, 41))
        self.pbadd.setObjectName("pbadd")
        self.gridLayout_3.addWidget(self.pbadd, 1, 3, 1, 1)
        self.pb4 = QtWidgets.QPushButton(self.centralwidget)
        self.pb4.setMinimumSize(QtCore.QSize(81, 41))
        self.pb4.setMaximumSize(QtCore.QSize(90, 41))
        self.pb4.setObjectName("pb4")
        self.gridLayout_3.addWidget(self.pb4, 2, 0, 1, 1)
        self.pb5 = QtWidgets.QPushButton(self.centralwidget)
        self.pb5.setMinimumSize(QtCore.QSize(81, 41))
        self.pb5.setMaximumSize(QtCore.QSize(90, 41))
        self.pb5.setObjectName("pb5")
        self.gridLayout_3.addWidget(self.pb5, 2, 1, 1, 1)
        self.pb6 = QtWidgets.QPushButton(self.centralwidget)
        self.pb6.setMinimumSize(QtCore.QSize(81, 41))
        self.pb6.setMaximumSize(QtCore.QSize(90, 41))
        self.pb6.setObjectName("pb6")
        self.gridLayout_3.addWidget(self.pb6, 2, 2, 1, 1)
        self.pbsubstract = QtWidgets.QPushButton(self.centralwidget)
        self.pbsubstract.setMinimumSize(QtCore.QSize(81, 41))
        self.pbsubstract.setMaximumSize(QtCore.QSize(90, 41))
        self.pbsubstract.setObjectName("pbsubstract")
        self.gridLayout_3.addWidget(self.pbsubstract, 2, 3, 1, 1)
        self.pb7 = QtWidgets.QPushButton(self.centralwidget)
        self.pb7.setMinimumSize(QtCore.QSize(81, 41))
        self.pb7.setMaximumSize(QtCore.QSize(90, 41))
        self.pb7.setObjectName("pb7")
        self.gridLayout_3.addWidget(self.pb7, 3, 0, 1, 1)
        self.pb8 = QtWidgets.QPushButton(self.centralwidget)
        self.pb8.setMinimumSize(QtCore.QSize(81, 41))
        self.pb8.setMaximumSize(QtCore.QSize(90, 41))
        self.pb8.setObjectName("pb8")
        self.gridLayout_3.addWidget(self.pb8, 3, 1, 1, 1)
        self.pb9 = QtWidgets.QPushButton(self.centralwidget)
        self.pb9.setMinimumSize(QtCore.QSize(81, 41))
        self.pb9.setMaximumSize(QtCore.QSize(90, 41))
        self.pb9.setObjectName("pb9")
        self.gridLayout_3.addWidget(self.pb9, 3, 2, 1, 1)
        self.pbmultiply = QtWidgets.QPushButton(self.centralwidget)
        self.pbmultiply.setMinimumSize(QtCore.QSize(81, 41))
        self.pbmultiply.setMaximumSize(QtCore.QSize(90, 41))
        self.pbmultiply.setObjectName("pbmultiply")
        self.gridLayout_3.addWidget(self.pbmultiply, 3, 3, 1, 1)
        self.pbclear = QtWidgets.QPushButton(self.centralwidget)
        self.pbclear.setMinimumSize(QtCore.QSize(81, 41))
        self.pbclear.setMaximumSize(QtCore.QSize(90, 41))
        self.pbclear.setObjectName("pbclear")
        self.gridLayout_3.addWidget(self.pbclear, 4, 0, 1, 1)
        self.pb0 = QtWidgets.QPushButton(self.centralwidget)
        self.pb0.setMinimumSize(QtCore.QSize(81, 41))
        self.pb0.setMaximumSize(QtCore.QSize(90, 41))
        self.pb0.setObjectName("pb0")
        self.gridLayout_3.addWidget(self.pb0, 4, 1, 1, 1)
        self.pbenter = QtWidgets.QPushButton(self.centralwidget)
        self.pbenter.setMinimumSize(QtCore.QSize(81, 41))
        self.pbenter.setMaximumSize(QtCore.QSize(90, 41))
        self.pbenter.setObjectName("pbenter")
        self.gridLayout_3.addWidget(self.pbenter, 4, 2, 1, 1)
        self.pbdivide = QtWidgets.QPushButton(self.centralwidget)
        self.pbdivide.setMinimumSize(QtCore.QSize(81, 41))
        self.pbdivide.setMaximumSize(QtCore.QSize(90, 41))
        self.pbdivide.setObjectName("pbdivide")
        self.gridLayout_3.addWidget(self.pbdivide, 4, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 403, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
#Declaring Necessary Variables
        self.leftoperand=np.float32(0.0)
        self.rightoperand=np.float32(0.0)
        self.result=np.float32(0.0)
        self.operator=0
#Making the Button Work
        self.pb1.clicked.connect(lambda:self.buttonevent(1))
        self.pb2.clicked.connect(lambda:self.buttonevent(2))
        self.pb3.clicked.connect(lambda:self.buttonevent(3))
        self.pb4.clicked.connect(lambda:self.buttonevent(4))
        self.pb5.clicked.connect(lambda:self.buttonevent(5))
        self.pb6.clicked.connect(lambda:self.buttonevent(6))
        self.pb7.clicked.connect(lambda:self.buttonevent(7))
        self.pb8.clicked.connect(lambda:self.buttonevent(8))
        self.pb9.clicked.connect(lambda:self.buttonevent(9))
        self.pb0.clicked.connect(lambda:self.buttonevent(0))
        self.pbadd.clicked.connect(lambda:self.operatorselection(1))
        self.pbsubstract.clicked.connect(lambda:self.operatorselection(2))
        self.pbmultiply.clicked.connect(lambda:self.operatorselection(3))
        self.pbdivide.clicked.connect(lambda:self.operatorselection(4))
        self.pbclear.clicked.connect(self.reset)
        self.pbenter.clicked.connect(self.calculation)
#Function Definition for the number buttons
    def buttonevent(self,number):
        self.result=0
        self.leftoperan=str(self.leftoperand)
        self.rightoperan=str(self.rightoperand)
        if self.leftoperand!=0 and self.operator==0 and self.rightoperand==0:
            self.leftoperan+=str(number)
            self.leftoperand=int(self.leftoperan)
            self.lcddisplay.display(self.leftoperand)
        elif self.leftoperand==0 and self.operator==0 and self.rightoperand==0:
            self.leftoperand=number
            self.lcddisplay.display(self.leftoperand)
        if self.leftoperand!=0 and self.operator!=0 and self.rightoperand!=0:
            self.rightoperan+=str(number)
            self.rightoperand=int(self.rightoperan)
            self.lcddisplay.display(self.rightoperand)
        elif self.leftoperand!=0 and self.operator!=0 and self.rightoperand==0:
            self.rightoperand=number
            self.lcddisplay.display(self.rightoperand)
        return
#Operator Selection using Buttons
    def operatorselection(self,opcode):
        if self.result!=0:
            self.leftoperand=self.result
            self.rightoperand=0
            self.result=0
        if opcode==1:
            self.operator=1
        if opcode==2:
            self.operator=2
        if opcode==3:
            self.operator=3
        if opcode==4:
            self.operator=4
        return
#Reset Button Defenition
    def reset(self):
        self.initalise=0
        self.leftoperand=self.initalise
        self.rightoperand=self.initalise
        self.operator=self.initalise
        self.result=self.initalise
        self.lcddisplay.display(self.initalise)
        return
#Enter button, calculation
    def calculation(self):
        if self.operator==1:
            self.result+=self.leftoperand+self.rightoperand
        if self.operator==2:
            self.result+=self.leftoperand-self.rightoperand
        if self.operator==3:
            self.result+=self.leftoperand*self.rightoperand
        if self.operator==4:
            self.result+=self.leftoperand/self.rightoperand
        self.lcddisplay.display(self.result)
        return
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pb1.setText(_translate("MainWindow", "1"))
        self.pb2.setText(_translate("MainWindow", "2"))
        self.pb3.setText(_translate("MainWindow", "3"))
        self.pbadd.setText(_translate("MainWindow", "+"))
        self.pb4.setText(_translate("MainWindow", "4"))
        self.pb5.setText(_translate("MainWindow", "5"))
        self.pb6.setText(_translate("MainWindow", "6"))
        self.pbsubstract.setText(_translate("MainWindow", "-"))
        self.pb7.setText(_translate("MainWindow", "7"))
        self.pb8.setText(_translate("MainWindow", "8"))
        self.pb9.setText(_translate("MainWindow", "9"))
        self.pbmultiply.setText(_translate("MainWindow", "x"))
        self.pbclear.setText(_translate("MainWindow", "Reset"))
        self.pb0.setText(_translate("MainWindow", "0"))
        self.pbenter.setText(_translate("MainWindow", "Enter"))
        self.pbdivide.setText(_translate("MainWindow", "/"))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())