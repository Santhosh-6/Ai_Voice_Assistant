from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_wizzenui(object):
    def setupUi(self, wizzenui):
        wizzenui.setObjectName("wizzenui")
        wizzenui.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        wizzenui.setWindowFlag(QtCore.Qt.WindowType.WindowStaysOnTopHint)
        wizzenui.move(0,0)#open position on left 
        wizzenui.resize(419, 376)
        wizzenui.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.settingsframe = QtWidgets.QFrame(wizzenui)
        self.settingsframe.setGeometry(QtCore.QRect(230, 30, 191, 181))
        self.settingsframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.settingsframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.settingsframe.setObjectName("settingsframe")
        self.frame = QtWidgets.QFrame(self.settingsframe)
        self.frame.setGeometry(QtCore.QRect(0, 0, 191, 181))
        self.frame.setStyleSheet("border: 1px solid white;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.closebutton=QtWidgets.QPushButton(self.frame)
        self.closebutton.setGeometry(QtCore.QRect(154,154,31,20))
        self.closebutton.setStyleSheet("color: rgb(255, 255, 255);\n"
                                       "font: 700 12pt \"Terminal\";\n"
                                       "background-color: rgb(0, 0, 0);\n"
                                       "border: none;")
        self.closebutton.setObjectName("closebutton")
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 151, 31))
        self.textEdit.setStyleSheet("border:none;\n"
"background-color:transparent;")
        self.textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.showicon = QtWidgets.QCheckBox(self.frame)
        self.showicon.setGeometry(QtCore.QRect(20, 50, 141, 31))
        self.showicon.setStyleSheet("border:none;\n"
"color: rgb(255, 255, 255);")
        self.showicon.setObjectName("showicon")
        self.mutewizzen = QtWidgets.QCheckBox(self.frame)
        self.mutewizzen.setGeometry(QtCore.QRect(20, 90, 141, 31))
        self.mutewizzen.setStyleSheet("border:none;\n"
"color: rgb(255, 255, 255);")
        self.mutewizzen.setObjectName("mutewizzen")
        self.showterminal = QtWidgets.QCheckBox(self.frame)
        self.showterminal.setGeometry(QtCore.QRect(20, 130, 141, 31))
        self.showterminal.setStyleSheet("border:none;\n"
"color: rgb(255, 255, 255);")
        self.showterminal.setObjectName("showterminal")
        self.heading = QtWidgets.QPushButton(wizzenui)
        self.heading.setGeometry(QtCore.QRect(0, 0, 211, 51))
        self.heading.setStyleSheet("border-image: url(D:/Visual Studio/Ai_Voice_Assistant/Resource/wizzen1.png);\n"
"")
        self.heading.setText("")
        self.heading.setObjectName("heading")
        self.listening = QtWidgets.QLabel(wizzenui)
        self.listening.setGeometry(QtCore.QRect(0, 50, 211, 161))
        self.listening.setText("")
        self.listening.setPixmap(QtGui.QPixmap("Resource\listening.gif"))
        self.listening.setScaledContents(True)
        self.listening.setObjectName("listening")
        self.loading = QtWidgets.QLabel(wizzenui)
        self.loading.setGeometry(QtCore.QRect(0, 50, 211, 161))
        self.loading.setText("")
        self.loading.setPixmap(QtGui.QPixmap("Resource\loading.gif"))
        self.loading.setScaledContents(True)
        self.loading.setObjectName("loading")
        self.sleeping = QtWidgets.QLabel(wizzenui)
        self.sleeping.setGeometry(QtCore.QRect(0, 50, 211, 161))
        self.sleeping.setText("")
        self.sleeping.setPixmap(QtGui.QPixmap("Resource\sleeping.gif"))
        self.sleeping.setScaledContents(True)
        self.sleeping.setObjectName("sleeping")
        self.speaking = QtWidgets.QLabel(wizzenui)
        self.speaking.setGeometry(QtCore.QRect(0, 50, 211, 161))
        self.speaking.setText("")
        self.speaking.setPixmap(QtGui.QPixmap("Resource\loading.gif"))
        self.speaking.setScaledContents(True)
        self.speaking.setObjectName("speaking")
        self.pushButton = QtWidgets.QPushButton(wizzenui)
        self.pushButton.setGeometry(QtCore.QRect(384, 0, 31, 24))
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 700 12pt \"Terminal\";\n"
"background-color: rgb(0, 0, 0);\n"
"border: none;")
        self.pushButton.setObjectName("pushButton")
        self.frame_2 = QtWidgets.QFrame(wizzenui)
        self.frame_2.setGeometry(QtCore.QRect(0, 220, 411, 161))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.terminaltext = QtWidgets.QPlainTextEdit(self.frame_2)
        self.terminaltext.setGeometry(QtCore.QRect(0, 20, 419, 137))
        self.terminaltext.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 11pt \"Trebuchet MS\";")
        self.terminaltext.setReadOnly(True)
        self.terminaltext.setObjectName("terminaltext")
        self.terminalhead = QtWidgets.QLineEdit(wizzenui)
        self.terminalhead.setGeometry(QtCore.QRect(0, 220, 420, 22))
        self.terminalhead.setStyleSheet("border:1px solid white;\n"
"font: 700 10pt \"Trebuchet MS\";\n"
"color: rgb(255, 255, 255);")
        self.terminalhead.setAlignment(QtCore.Qt.AlignCenter)
        self.terminalhead.setReadOnly(True)
        self.terminalhead.setObjectName("terminalhead")

        self.retranslateUi(wizzenui)
        QtCore.QMetaObject.connectSlotsByName(wizzenui)

    def retranslateUi(self, wizzenui):
        _translate = QtCore.QCoreApplication.translate
        wizzenui.setWindowTitle(_translate("wizzenui", "wizzenui"))
        self.textEdit.setHtml(_translate("wizzenui", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:700; color:#ffffff;\">Settings</span></p></body></html>"))
        self.showicon.setText(_translate("wizzenui", "Show Status Icons"))
        self.mutewizzen.setText(_translate("wizzenui", "Mute Wizzen"))
        self.showterminal.setText(_translate("wizzenui", "Show Terminal"))
        self.closebutton.setText(_translate("wizzenui","X"))
        self.pushButton.setText(_translate("wizzenui", "-"))
        self.terminalhead.setText(_translate("wizzenui", "Wizzen Terminal"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    wizzenui = QtWidgets.QWidget()
    ui = Ui_wizzenui()
    ui.setupUi(wizzenui)
    wizzenui.show()
    sys.exit(app.exec_())
