from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import pyttsx3
import time


#This is the pyttsx3 speech engine
engine = pyttsx3.init()

#To check if the delay time is valid or not
def is_integer(n):
	try:
		if(int(n)>=0 and int(n)<=10):
			return True
		else:
			return False
	except ValueError:
		return False


#Implementing the application with PyQt5
class Ui_PythonSpeaker(object):
	def setupUi(self, PythonSpeaker):
		PythonSpeaker.setObjectName("PythonSpeaker")
		PythonSpeaker.resize(789, 202)
		self.centralwidget = QtWidgets.QWidget(PythonSpeaker)
		self.centralwidget.setObjectName("centralwidget")
		self.pushButton = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton.setGeometry(QtCore.QRect(590, 60, 151, 81))
		font = QtGui.QFont()
		font.setPointSize(16)
		self.pushButton.setFont(font)
		self.pushButton.setObjectName("pushButton")
		self.textEdit1 = QtWidgets.QTextEdit(self.centralwidget)
		self.textEdit1.setGeometry(QtCore.QRect(20, 50, 531, 121))
		self.textEdit1.setObjectName("textEdit1")
		self.textEdit2 = QtWidgets.QTextEdit(self.centralwidget)
		self.textEdit2.setGeometry(QtCore.QRect(170, 10, 41, 31))
		self.textEdit2.setObjectName("textEdit2")
		self.label = QtWidgets.QLabel(self.centralwidget)
		self.label.setGeometry(QtCore.QRect(70, 10, 91, 31))
		self.label.setObjectName("label")
		PythonSpeaker.setCentralWidget(self.centralwidget)
		self.statusbar = QtWidgets.QStatusBar(PythonSpeaker)
		self.statusbar.setObjectName("statusbar")
		PythonSpeaker.setStatusBar(self.statusbar)

		self.retranslateUi(PythonSpeaker)
		QtCore.QMetaObject.connectSlotsByName(PythonSpeaker)

	def retranslateUi(self, PythonSpeaker):
		_translate = QtCore.QCoreApplication.translate
		PythonSpeaker.setWindowTitle(_translate("PythonSpeaker", "Python Speaker"))
		PythonSpeaker.setStatusTip(_translate("PythonSpeaker", "Delay time - To delay the speaking (in sec)"))
		self.pushButton.setStatusTip(_translate("PythonSpeaker", "Click me to speak-out"))
		self.pushButton.setText(_translate("PythonSpeaker", "Speak"))
		self.textEdit1.setStatusTip(_translate("PythonSpeaker", "Type your words here !"))
		self.textEdit2.setStatusTip(_translate("PythonSpeaker", "Delay time - To delay the speaking from 0 to 10 sec"))
		self.label.setText(_translate("PythonSpeaker", "Set delay time :"))

		self.pushButton.clicked.connect(self.on_click)

	#This error dialog is shown if delay time is a invalid entry
	def error(self):
		errorDialog = QMessageBox()
		errorDialog.setIcon(QMessageBox.Critical)
		errorDialog.setText("Error in delay time. Make sure delay is between 0 and 10 sec")
		errorDialog.setWindowTitle("Error reading")
		errorDialog.exec_()

	def on_click(self):
		myText = self.textEdit1.toPlainText()
		delayTime = self.textEdit2.toPlainText()
		if(is_integer(delayTime) == False):
			self.error()
		else:
			time.sleep(int(delayTime))
			engine.say(myText)
			engine.runAndWait()


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	PythonSpeaker = QtWidgets.QMainWindow()
	ui = Ui_PythonSpeaker()
	ui.setupUi(PythonSpeaker)
	PythonSpeaker.show()
	sys.exit(app.exec_())
