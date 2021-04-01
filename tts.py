from PyQt5 import QtCore, QtGui, QtWidgets
import pyttsx3
import PyPDF2

engine = pyttsx3.init()


# speech engine properties
def setSpeechProp(rateValue, volumeValue, VoiceId):
    engine.setProperty('rate', rateValue)        #default voice rate would be 200
    engine.setProperty('volume' , volumeValue)   #setting up volume level  between 0 and 1
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[VoiceId].id)     #VoiceId = 0 for male voice and 1 for female voice

def speak(myText):
    engine.say(myText)
    engine.runAndWait()

def getPageText(nameOfPdf, pageNo):
    inputPdf = PyPDF2.PdfFileReader(open(nameOfPdf, "rb"))

    # a page object pointing to the page with pageNo
    # doesn't support for images
    currPage = inputPdf.getPage(pageNo)

    # text strored in this string
    pageText = currPage.extractText()
    return(pageText)

def readPageAloud(nameOfPdf, pageNum):
    pageText = getPageText(nameOfPdf, pageNum)
    speak(pageText)

def readPdf(nameOfPdf):
    inputPdf = PyPDF2.PdfFileReader(open(nameOfPdf, "rb"))

    noOfPages = inputPdf.getNumPages()

    for i in range(noOfPages):
        readPageAloud(nameOfPdf, i)

def readPdfFrom(nameOfPdf, startPgNum):
    inputPdf = PyPDF2.PdfFileReader(open(nameOfPdf, "rb"))

    noOfPages = inputPdf.getNumPages()

    if(startPgNum < noOfPages):
        for i in range(startPgNum, noOfPages):
            readPageAloud(nameOfPdf, i)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(554, 348)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit1 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit1.setGeometry(QtCore.QRect(140, 30, 191, 31))
        self.textEdit1.setObjectName("textEdit1")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(30, 30, 111, 31))
        self.label1.setObjectName("label1")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(200, 100, 151, 51))
        self.pushButton.setObjectName("pushButton")
        self.volSlider = QtWidgets.QSlider(self.centralwidget)
        self.volSlider.setGeometry(QtCore.QRect(430, 80, 22, 160))
        self.volSlider.setMaximum(100)
        self.volSlider.setOrientation(QtCore.Qt.Vertical)
        self.volSlider.setObjectName("volSlider")
        self.textEdit2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit2.setGeometry(QtCore.QRect(70, 110, 81, 31))
        self.textEdit2.setObjectName("textEdit2")
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(20, 110, 55, 31))
        self.label2.setObjectName("label2")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(50, 170, 95, 20))
        self.radioButton.setObjectName("radioButton")
        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(420, 250, 55, 16))
        self.label3.setObjectName("label3")
        self.textEdit3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit3.setGeometry(QtCore.QRect(440, 30, 51, 31))
        self.textEdit3.setObjectName("textEdit3")
        self.label4 = QtWidgets.QLabel(self.centralwidget)
        self.label4.setGeometry(QtCore.QRect(370, 40, 71, 20))
        self.label4.setObjectName("label4")
        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(210, 190, 131, 51))
        self.pushButton1.setObjectName("pushButton1")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 554, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PDF reader"))
        self.label1.setText(_translate("MainWindow", "PDF name"))
        self.pushButton.setText(_translate("MainWindow", "SPEAK"))
        self.label2.setText(_translate("MainWindow", "Rate"))
        self.radioButton.setText(_translate("MainWindow", "Male Voice"))
        self.label3.setText(_translate("MainWindow", "Volume"))
        self.label4.setText(_translate("MainWindow", "From Page"))
        self.pushButton1.setText(_translate("MainWindow", "STOP"))
        self.pushButton.clicked.connect(self.on_click)
        self.pushButton1.clicked.connect(self.stopFun)

    def on_click(self):
        startPgNum = self.textEdit3.toPlainText()
        rateVal = self.textEdit2.toPlainText()
        volumeVal = self.volSlider.value() / 100.0
        pdfName = self.textEdit1.toPlainText()

        if(self.radioButton.isChecked()==True):
            voiceId=0
        else:
            voiceId=1
        setSpeechProp(rateVal, volumeVal, voiceId)

        readPdfFrom(pdfName, int(startPgNum))
    
    def stopFun(self):
        engine.stop()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    pdfReader = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(pdfReader)
    pdfReader.show()
    sys.exit(app.exec_())

