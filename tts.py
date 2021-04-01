from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import pyttsx3
import time


#This is the pyttsx3 speech engine
engine = pyttsx3.init()

#To check if the delay time is valid or not (i.e, should be a positive number from 0 to 10 sec)
def is_valid(n):
	try:
		if(int(n)>=0 and int(n)<=10):
			return True
		else:
			return False
	except ValueError:
		return False

class Ui_PythonSpeaker(object):
	def setupUi(self, PythonSpeaker):
		PythonSpeaker.setObjectName("PythonSpeaker")
		PythonSpeaker.resize(758, 244)
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
		self.delayEdit = QtWidgets.QTextEdit(self.centralwidget)
		self.delayEdit.setGeometry(QtCore.QRect(170, 10, 41, 31))
		self.delayEdit.setObjectName("delayEdit")
		self.label = QtWidgets.QLabel(self.centralwidget)
		self.label.setGeometry(QtCore.QRect(70, 10, 91, 31))
		self.label.setObjectName("label")
		self.volumeSlider = QtWidgets.QSlider(self.centralwidget)
		self.volumeSlider.setGeometry(QtCore.QRect(110, 190, 160, 22))
		self.volumeSlider.setOrientation(QtCore.Qt.Horizontal)
		self.volumeSlider.setObjectName("volumeSlider")
		self.label_2 = QtWidgets.QLabel(self.centralwidget)
		self.label_2.setGeometry(QtCore.QRect(40, 190, 55, 16))
		self.label_2.setObjectName("label_2")
		self.label_3 = QtWidgets.QLabel(self.centralwidget)
		self.label_3.setGeometry(QtCore.QRect(320, 20, 61, 16))
		self.label_3.setObjectName("label_3")
		self.rateSlider = QtWidgets.QSlider(self.centralwidget)
		self.rateSlider.setGeometry(QtCore.QRect(400, 20, 160, 22))
		self.rateSlider.setOrientation(QtCore.Qt.Horizontal)
		self.rateSlider.setObjectName("rateSlider")
		self.maleVoiceCheckbox = QtWidgets.QCheckBox(self.centralwidget)
		self.maleVoiceCheckbox.setGeometry(QtCore.QRect(410, 190, 101, 20))
		self.maleVoiceCheckbox.setObjectName("maleVoiceCheckbox")
		self.femaleVoiceCheckbox = QtWidgets.QCheckBox(self.centralwidget)
		self.femaleVoiceCheckbox.setGeometry(QtCore.QRect(520, 190, 111, 20))
		self.femaleVoiceCheckbox.setObjectName("femaleVoiceCheckbox")
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
		self.delayEdit.setStatusTip(_translate("PythonSpeaker", "Delay time - To delay the speaking (in sec)"))
		self.label.setText(_translate("PythonSpeaker", "Set delay time :"))
		self.volumeSlider.setStatusTip(_translate("PythonSpeaker", "Slide me to chage the volume"))
		self.label_2.setText(_translate("PythonSpeaker", "Volume :"))
		self.label_3.setText(_translate("PythonSpeaker", "Set Rate :"))
		self.rateSlider.setStatusTip(_translate("PythonSpeaker", "Set your voice rate here"))
		self.maleVoiceCheckbox.setText(_translate("PythonSpeaker", "Male Voice"))
		self.femaleVoiceCheckbox.setText(_translate("PythonSpeaker", "Female Voice"))

		self.pushButton.clicked.connect(self.on_click)
		self.delayEdit.setText('0')             #Default delay time
		self.rateSlider.setMinimum(1)
		self.rateSlider.setMaximum(250)
		self.rateSlider.setValue(175)           #This is the default state of rate slider
		self.volumeSlider.setValue(100)         #This is the default state of volume slider
		self.maleVoiceCheckbox.setChecked(True)

	#This error is shown if the text-field is empty
	def errorEmptyText(self, message):
		errorDialog = QMessageBox()
		errorDialog.setIcon(QMessageBox.Critical)
		errorDialog.setText(message)
		errorDialog.setWindowTitle("Reading error")
		errorDialog.exec_()

	def on_click(self):
		myText = self.textEdit1.toPlainText()
		delayTime = self.delayEdit.toPlainText()
		rateValue = self.rateSlider.value()
		volumeValue = self.volumeSlider.value() / 100.0

		if(is_valid(delayTime) == False):
			self.errorEmptyText("Error reading delay time. Make sure delay time is an integer between 0 and 10 sec")
			return
		if(myText == ''):
			self.errorEmptyText("Please enter text to be spoken!!")
		else:
			engine.setProperty('rate', rateValue)        #default voice rate would be 200
			engine.setProperty('volume' , volumeValue)   #setting up volume level  between 0 and 1
			if(self.maleVoiceCheckbox.isChecked() == True and self.femaleVoiceCheckbox.isChecked() == False):
				VoiceId = 0
			elif(self.femaleVoiceCheckbox.isChecked() == True and self.maleVoiceCheckbox.isChecked() == False):
				VoiceId = 1
			else:
				self.maleVoiceCheckbox.setChecked(True)
				self.femaleVoiceCheckbox.setChecked(False)
				VoiceId = 0                             #Defaluts to male voice if both are selected or if none are selected

			voices = engine.getProperty('voices')
			engine.setProperty('voice', voices[VoiceId].id)     #VoiceId = 0 for male voice and 1 for female voice
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

