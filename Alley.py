   #thalaivaar

import speech_recognition as sr
import datetime
import pyttsx3
import pywhatkit
import pyaudio
import wikipedia

listener = sr.Recognizer()
reply = pyttsx3.init()
voices = reply.getProperty('voices')
reply.setProperty('voice', voices[1].id)


def talk(text):
    reply.say(text)
    reply.runAndWait()
def takecommand():
    try:
        with sr.Microphone() as source:
            print("listening....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            print(command)
    except:
        pass
    return command
def runcommand():
    command = takecommand()
    command = command.lower()

    if 'propose' in command:
            command = command.replace('propose', ' ')
            proposal = command+" i love you"
            talk(proposal)
            print(proposal)
    elif 'play' in command:
            command = command.replace('play', ' ')
            talk("playing"+command)
            pywhatkit.playonyt(command)

    elif 'date and time' in command:
            command = datetime.datetime.now()
            talk(command)
            print(command)
    elif 'date' in command:
            command = datetime.date.today()
            talk(command)
            print(command)

    elif 'time' in command:
            command = datetime
            talk(command)
            print(command)

    elif 'who' or 'where' or 'when' or 'tell' or 'what' or 'how' or 'explain' or 'which' in command:
            ans = wikipedia.summary(command,1)
            print(ans)
            talk(ans)
            talk(bye)

    elif 'send whatsapp message' in command:
            pywhatkit.sendwhatmsg('+91xxxxxxxxxx', 'hello','''hour,minutes''' )


    else:
        print("cant recognize")
        
runcommand()



