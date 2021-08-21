from PyQt5 import QtCore, QtGui, QtWidgets
import subprocess
import webbrowser
from playsound import playsound



class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(395, 506)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("arp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setAutoFillBackground(False)
        self.commandbox = QtWidgets.QLineEdit(Dialog)
        self.commandbox.setGeometry(QtCore.QRect(20, 340, 331, 31))
        self.commandbox.setObjectName("commandbox")
        self.enterbutton = QtWidgets.QPushButton(Dialog)
        self.enterbutton.setGeometry(QtCore.QRect(350, 340, 21, 31))
        self.enterbutton.setObjectName("enterbutton")
        self.enterbutton.clicked.connect(self.on_click)#connecting button to function
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(180, 380, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(29)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.micbutton = QtWidgets.QPushButton(Dialog)
        self.micbutton.setGeometry(QtCore.QRect(130, 430, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(38)
        self.micbutton.setFont(font)
        self.micbutton.setObjectName("micbutton")
        self.micbutton.clicked.connect(self.on_click_micbutton)#connecting button to function
        self.photo = QtWidgets.QLabel(Dialog)
        self.photo.setGeometry(QtCore.QRect(70, 20, 331, 301))
        self.photo.setText("")
        self.photo.setObjectName("photo")
        qpixmap=QtGui.QPixmap("arp.png")
        self.photo.setPixmap(qpixmap)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        self.enterbutton.setText(_translate("Dialog", ">"))
        self.label_2.setText(_translate("Dialog", "or"))
        self.micbutton.setText(_translate("Dialog", "🎙"))
    


    def on_click(self):
        textboxValue = a = self.commandbox.text()
        a=a.lower()
        #typed commands
        if a=="camera":
            subprocess.call("cheese")
        elif a=="edge":
            subprocess.call("microsoft-edge-beta")
        elif a=="google":
            webbrowser.open("https://google.com")
        elif a=="class" or a=="classroom":
            webbrowser.open("https://classroom.google.com/u/0/h")
        elif a=="youtube":
            webbrowser.open("https://www.youtube.com/")
        elif a=="w":
            webbrowser.open("https://web.whatsapp.com/")
        elif a=="telegram":
            webbrowser.open("https://web.telegram.org/#/im")
        elif "g?" in a:# google search
            a = a.replace('g?','')      
            a="https://www.google.com/search?q="+a
            webbrowser.open(a)         
        elif a=="droidcam":
            subprocess.call("droidcam")
        elif a=="current time":
            webbrowser.open("https://www.timeanddate.com/worldclock/fullscreen.html?n=176")
        else:
            a="https://www.google.com/search?q="+a
            webbrowser.open(a)  

            
            
        playsound('sounds/ok ok i got that.mp3')
        self.commandbox.clear()

    def on_click_micbutton(self):
        import speech_recognition as sr
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Talk")
            audio_text = r.listen(source)
            print("Time over, thanks")
            print(r.recognize_google(audio_text))  
        a=(r.recognize_google(audio_text)) 
        a=a.lower() 
        if  a.split()[0]=="open":
            a = a.replace('open','')      
        b=True # for checking if it has got into the custom sound how are you and who are you
        # all voice commands
        if "camera" in a:
            subprocess.call("cheese")
        elif "microsoft"in a and "edge" in a:
            subprocess.call("microsoft-edge-beta")
        elif "google" in a:
            webbrowser.open("https://google.com")
        elif "class" in a or "classroom" in a:
            webbrowser.open("https://classroom.google.com/u/0/h")
        elif "youtube" in a:
            webbrowser.open("https://www.youtube.com/")
        elif "whatsapp" in a or "whattsapp" in a:
            webbrowser.open("https://web.whatsapp.com/")
        elif "telegram" in a:
            webbrowser.open("https://web.telegram.org/#/im")
        elif "g?" in a:# google search
            a = a.replace('g?','')      
            a="https://www.google.com/search?q="+a
            webbrowser.open(a)         
        elif "droidcam" in a:
            subprocess.call("droidcam")
        elif "current time" in a:
            webbrowser.open("https://www.timeanddate.com/worldclock/fullscreen.html?n=176")
        elif "how are you" in a or "who are you" in a:
            b=False
            if "how are you" in a:
                playsound('sounds/how are you ?.mp3')
            elif "who are you" in a:
                playsound('sounds/who are you ?.mp3')          
        else:
            a="https://www.google.com/search?q="+a
            webbrowser.open(a)  
            
        
        if b:# if  it did not enter how are you  or who are you it will play sound and if it entered it will not play
            playsound('sounds/ok ok i got that.mp3')



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
