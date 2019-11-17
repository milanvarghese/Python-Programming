from PyQt5 import QtCore, QtGui, QtWidgets
import speech_recognition as sr

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(524, 179)
        Form.setMinimumSize(QtCore.QSize(524, 179))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; text-decoration: underline; vertical-align:super;\">Google Web - Speech to Text</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.pushButton.setText(_translate("Form", "Record"))

        self.text= self.pushButton.clicked.connect(lambda:self.buttonevent(speech_to_text()))
        self.label_2.setText(_translate(self.text))
    
    def speech_to_text():
        r = sr.Recognizer()
        mic = sr.Microphone()
        mic = sr.Microphone(device_index=1)
        with mic as source:
            audio = r.listen(source)
        text=r.recognize_google(audio)
        return text

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())