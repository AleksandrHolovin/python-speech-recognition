import speech_recognition as sr
import os
import sys
import webbrowser
import pyttsx3


def talk(speech):
    print(speech)
    engine = pyttsx3.init()
    engine.say(speech)
    engine.runAndWait()


def command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        talk('Hi, Say something!')
        r.pause_threshold = 0.5
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try: 
        task = r.recognize_google(audio).lower()
        print('You say ' + task)
    except sr.UnknownValueError: 
        talk('I dont understand you')
        talk('Just opening')
        url = 'https//google.com'
        webbrowser.open(url)
    elif 'stop' in task:
        talk('Yes ofc')
        sys.exit()

while True:
    doTask(command())