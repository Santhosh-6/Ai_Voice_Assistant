import PyQt5
import PyQt5.QtCore
import pyttsx3  
from datetime import datetime
from dotenv import load_dotenv
import speech_recognition as sr
from functions.os_ops import  open_notepad, open_cmd,open_camera
from functions.online_ops import search_google, play_youtube,get_random_advice,get_random_joke
import sys
import os
import google.generativeai as genai
from template import Ui_wizzenui

from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtGui

load_dotenv()
USERNAME = os.getenv('USER')
BOTNAME = os.getenv('BOTNAME')

# Initialize text-to-speech engine
engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 190)
engine.setProperty('volume', 1.0)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def s(text):
    if startExecution.muteState=='yes':
        pass
    else:
        ui.updategifsdynamically('speaking')
        engine.say(text)
        engine.runAndWait()

class WizzenMainClass(QThread):
    def __init__(self):
        super(WizzenMainClass,self).__init__()
        self.muteState=None

    def greet_user(self):
        hour = datetime.now().hour
        if 6 <= hour < 12:
            s(f"Good morning {USERNAME}")
        elif 12 <= hour < 16:
            s(f"Good afternoon {USERNAME}")
        elif 16 <= hour < 19:
            s(f"Good evening {USERNAME}")
        s(f"I am {BOTNAME}. How may I help you?")

    def gpt(self):
        try:
            genai.configure(api_key=("YOUR_API_KEY"))  

            generation_config = {
                "temperature": 1,
                "top_p": 1,
                "max_output_tokens": 2048,
                "response_mime_type": "text/plain",
            }

            model = genai.GenerativeModel(
                model_name="gemini-1.0-pro",
                generation_config=generation_config,
            )

            history = []
            r = sr.Recognizer()
            
            with sr.Microphone() as scr:
                ui.terminalprint("Listening...")
                ui.updategifsdynamically('listening')
                r.pause_threshold = 1
                audio = r.listen(scr)
            try:
                print("Recognizing...")
                ui.updategifsdynamically('loading')
                query = r.recognize_google(audio, language='en-in')
            except sr.UnknownValueError:
                s("Sorry, I couldn't understand you. Could you repeat that?")
                return
            print(ui.terminalprint(query))

            while True:
                chat_session = model.start_chat(history=history)
                response = chat_session.send_message(query)
                print(f"Wizzen: {response.text}")
                history.append({'role': 'user', "parts": [query]})
                history.append({'role': 'model', "parts": [response.text]})
                s(response.text)
                ui.terminalprint(response.text)
                
                if 'thanks for giving information' in query:
                    break
                else:
                    self.gpt()# Exit function if the user says 'thanks for giving information'
                while True:
                    query = self.user_inp()
                    if 'open notepad' in query:
                        open_notepad()
                    elif 'open cmd' in query:
                        open_cmd()
                    elif 'open camera' in query:
                        open_camera()    
                    elif 'youtube' in query:
                        s('What do you want to play on YouTube, sir?')
                        video = self.user_inp()
                        if video != 'None':
                            play_youtube(video)
                    elif 'search on google' in query:
                        s('What do you want to search on Google, sir?')
                        search_query = self.user_inp()
                        if search_query != 'None':
                            search_google(search_query)
                    elif 'joke' in query:
                        s(f"Hope you like this one sir")
                        joke = get_random_joke()
                        s(joke)
                        s("For your convenience, I am printing it on the screen sir.")
                        ui.terminalprint(joke)   
                    elif "advice" in query:
                        s(f"Here's an advice for you, sir")
                        advice = get_random_advice()
                        s(advice)
                        s("For your convenience, I am printing it on the screen sir.")
                        ui.terminalprint(advice)            
                    elif 'generate' in query or 'write' in query:
                        s('What do you want to generate, sir?')
                        self.gpt()

        except Exception as e:
            print(f"An error occurred with the GPT generation: {e}")

    def user_inp(self):
        ui.terminalprint("Listening...")
        ui.updategifsdynamically('listening')
        r = sr.Recognizer()
        with sr.Microphone() as scr:
            r.pause_threshold = 1
            audio = r.listen(scr)
            checkM=self.checkMuteStatus()
            if checkM:
                print('none')
                ui.updategifsdynamically('sleeping')
                pass
            else:
                try:
                    print("Recognizing...")
                    ui.updategifsdynamically('loading')
                    query = r.recognize_google(audio, language='en-in')
                    ui.terminalprint(query)
                    if 'exit' in query or 'stop' in query:   
                        hour = datetime.now().hour
                        farewell_message = "Good Night" if hour >= 21 else "Have a good day"
                        s(f"{farewell_message} {USERNAME}, take care.")
                        ui.updategifsdynamically('sleeping')
                        exit()  # Properly exit the application
                    return query.lower()
                except sr.UnknownValueError:
                    s('Sorry, I could not understand. Could you please say that again?')
                    return 'None'     

    def run_wizzen(self):
        while True:
            checkMute=self.checkMuteStatus()
            if not checkMute:
                query = self.user_inp()
                if query == 'None':
                    continue
                if 'wake up buddy' in query:
                    self.greet_user()
                elif 'open notepad' in query:
                    open_notepad()
                elif 'open cmd' in query:
                    open_cmd()
                elif 'open camera' in query:
                    open_camera()    
                elif 'youtube' in query:
                    s('What do you want to play on YouTube, sir?')
                    video = self.user_inp()
                    if video != 'None':
                        play_youtube(video)
                elif 'search on google' in query:
                    s('What do you want to search on Google, sir?')
                    search_query = self.user_inp()
                    if search_query != 'None':
                        search_google(search_query)
                elif 'joke' in query:
                    s(f"Hope you like this one sir")
                    joke = get_random_joke()
                    s(joke)
                    s("For your convenience, I am printing it on the screen sir.")
                    ui.terminalprint(joke)   
                elif "advice" in query:
                    s(f"Here's an advice for you, sir")
                    advice = get_random_advice()
                    s(advice)
                    s("For your convenience, I am printing it on the screen sir.")
                    ui.terminalprint(advice)            
                elif 'generate' in query or 'write' in query:
                    s('What do you want to generate, sir?')
                    self.gpt()
            else:
                pass

    def toggleMute(self,state):
        if state:
            self.muteState='yes'
            ui.terminalprint('Muted')
            ui.updategifsdynamically('sleeping')
        else:
            self.muteState='no'
            ui.terminalprint('active sir')
            s('active sir')

    def checkMuteStatus(self):
        checkMute=ui.wizzenUI.mutewizzen.checkState()
        if checkMute==0:
            return False
        else:
            return True   
        
    def run(self):
        self.run_wizzen()

startExecution = WizzenMainClass()

class UiWizzen(QMainWindow):
    def __init__(self):
        super(UiWizzen,self).__init__()
        self.oldPosition=PyQt5.QtCore.QPoint()
        self.wizzenUI = Ui_wizzenui()
        self.wizzenUI.setupUi(self)
        #self.showStatusIcons=False   
        self.wizzenUI.showicon.stateChanged.connect(self.showIconToggle)   
        self.wizzenUI.showterminal.stateChanged.connect(self.showTerminalToggle)
        self.wizzenUI.mutewizzen.stateChanged.connect(self.toggleMuteBTN)
        self.wizzenUI.closebutton.clicked.connect(self.close)
        self.wizzenUI.pushButton.clicked.connect(lambda: self.changewinsize('min'))
        self.wizzenUI.heading.clicked.connect(lambda: self.changewinsize('full'))

        self.runAllGIFs()
    
    def toggleMuteBTN(self,checked):
        if checked:
            WizzenMainClass.toggleMute(self,True)
        else:
            WizzenMainClass.toggleMute(self,False)    

    def showTerminalToggle(self,checked):
        if checked:
            self.showTerminal=True
            self.changewinsize('full')
        else:
            self.showTerminal=False
            self.resize(415,220)    

    def showIconToggle(self,checked):
        if checked:
            self.showStatusIcons=True#variable showstatusicon
        else:
            self.showStatusIcons=False    
    
    def changewinsize(self, type):
        if type == 'full':
            self.resize(419, 376)
        elif type == 'min':
            if not self.showStatusIcons:
               self.resize(211, 51)
            else:
                self.resize(212,215)   

    def runAllGIFs(self):
        self.wizzenUI.listeningMovie = QtGui.QMovie("Resource\listening.gif")
        self.wizzenUI.listening.setMovie(self.wizzenUI.listeningMovie)
        self.wizzenUI.listeningMovie.start()

        self.wizzenUI.speakingMovie = QtGui.QMovie("Resource\speaking.gif")
        self.wizzenUI.speaking.setMovie(self.wizzenUI.speakingMovie)
        self.wizzenUI.speakingMovie.start()

        self.wizzenUI.loadingMovie = QtGui.QMovie("Resource\loading.gif")
        self.wizzenUI.loading.setMovie(self.wizzenUI.loadingMovie)
        self.wizzenUI.loadingMovie.start()

        self.wizzenUI.sleepingMovie = QtGui.QMovie("Resource\sleeping.gif")
        self.wizzenUI.sleeping.setMovie(self.wizzenUI.sleepingMovie)
        self.wizzenUI.sleepingMovie.start()

        startExecution.start()

    def updategifsdynamically(self, state):
        self.wizzenUI.listening.hide()
        self.wizzenUI.speaking.hide()
        self.wizzenUI.loading.hide()
        self.wizzenUI.sleeping.hide()

        if state == 'speaking':
            self.wizzenUI.speaking.show()
        elif state == 'listening':
            self.wizzenUI.listening.show()
        elif state == 'loading':
            self.wizzenUI.loading.show()
        elif state == 'sleeping':
            self.wizzenUI.sleeping.show()

    def terminalprint(self, text):
        self.wizzenUI.terminaltext.appendPlainText(text)
    
    def mousePressEvent(self, value):
        self.oldPosition=value.globalPos()

    def mouseMoveEvent(self, value):
        d=PyQt5.QtCore.QPoint(value.globalPos()-self.oldPosition)
        self.move(self.x()+d.x(),self.y()+d.y())
        self.oldPosition=value.globalPos()    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = UiWizzen()
    ui.resize(218, 219)
    ui.show()
    sys.exit(app.exec_())
