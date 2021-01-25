"""
read commands.txt and requirements.txt before using this
"""

from PyQt5 import QtWidgets, QtGui,QtCore
from PyQt5.QtGui import QMovie
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
import pyttsx3
import speech_recognition as sr
import os
import time
import webbrowser
import datetime
import wikipedia
import smtplib
import pyjokes


flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',180)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak("Good morning, How may I help you?")
    elif hour>=12 and hour<18:
        speak("Good Afternoon, How may I help you?")
    else:
        speak("Good evening, How may I help you?")


class mainT(QThread):
    def __init__(self):
        super(mainT,self).__init__()
    
    def run(self):
        self.JARVIS()
    
    def STT(self):
        R = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listning...........")
            audio = R.listen(source)
        try:
            print("Recognising")
            text = R.recognize_google(audio,language='en-in')
            print(">> ",text)
        except Exception:
            speak("Sorry I did not get that")
            return "None"
        text = text.lower()
        return text

    def JARVIS(self):
        wish()
        while True:
            self.query = self.STT()
            if 'wikipedia' in self.query:  #if wikipedia found in the query then this block will be executed
                speak('Searching Wikipedia...')
                self.query = self.query.replace("wikipedia", "")
                self.query = self.query.replace("search","")
                self.query = self.query.replace("in","")
                results = wikipedia.summary(query, sentences=5) 
                speak("According to Wikipedia")
                print(results)
                speak(results)


            elif 'open youtube' in self.query:
                webbrowser.open("youtube.com")
                speak("opening youtube")

            elif 'open google' in self.query:
                webbrowser.open("google.com")
                speak("opening google")

            elif 'open stackoverflow' in self.query:
                webbrowser.open("stackoverflow.com")
                speak("opening stackoverflow")

            elif 'open github' in self.query:
                webbrowser.open("github.com")
                speak("opening github")

            elif 'open maps' in self.query:
                webbrowser.open("abhijeet-maps.netlify.app")#This a maps clone if you didn't like this u can change the url.
                speak("opening maps-clone")

            elif 'play music' in self.query:
                music_dir = 'D:\\Music' #change to the folder where your music is stored
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[0]))
                speak("playing music")

            elif 'the time' in self.query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"The time is {strTime}")

            elif 'open code' in self.query:
                code_path = "E:\\VS Code\\Code.exe" #change to the path in your computer
                os.startfile(code_path)
                speak("opening code")

            elif 'joke' in self.query: 
                speak(pyjokes.get_joke())

            elif 'meeting' in self.query:
                webbrowser.open("abhijeet-zoom.herokuapp.com") #This is a zoom-clone made by us If it blows up of you didn't like it you can change it.
                speak("starting a meeting")


FROM_MAIN,_ = loadUiType(os.path.join(os.path.dirname(__file__),"./scifi.ui"))

class Main(QMainWindow,FROM_MAIN):
    def __init__(self,parent=None):
        super(Main,self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(1920,1080)
        self.label_7 = QLabel
        self.exitB.setStyleSheet("background-image:url(./lib/exit - Copy.png);\n"
        "border:none;")
        self.exitB.clicked.connect(self.close)
        self.setWindowFlags(flags)
        Dspeak = mainT()
        self.label_7 = QMovie("./lib/gifloader.gif", QByteArray(), self)
        self.label_7.setCacheMode(QMovie.CacheAll)
        self.label_4.setMovie(self.label_7)
        self.label_7.start()

        self.ts = time.strftime("%A, %d %B")

        Dspeak.start()
        self.label.setPixmap(QPixmap("./lib/tuse.png"))
        self.label_5.setText("<font size=8 color='white'>"+self.ts+"</font>")
        self.label_5.setFont(QFont(QFont('Acens',8)))


app = QtWidgets.QApplication(sys.argv)
main = Main()
main.show()
exit(app.exec_())