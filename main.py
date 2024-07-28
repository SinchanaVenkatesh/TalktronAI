import os

import pyttsx3
import speech_recognition as sr
import webbrowser
import openai
import datetime
import subprocess

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language='en-in')
            print(f'User said: {query}')
            return query
        except Exception as e:
            return 'sorry, TalkTron could not understand'
if __name__ == '__main__':
    print('PyCharm')
    say('Hello I am TalkTron A I')
    while True:
        print("Listening...")
        query = takeCommand()
        sites =[['youtube', 'https://www.youtube.com'], ['wikipedia', 'https://wikipedia.com'], ['google', 'https://www.google.com']]
        #-----sites------
        for site in sites:
            if f'Open {site[0]}'.lower() in query.lower():
                say(f'Opening {site[0]}')
                webbrowser.open(site[1])
        #-----music-----
        if 'play music' in query:
            musicPath=r'C:\Users\Sinchana\Downloads\WestCoast.mp3'
            os.startfile(musicPath)
        #-----time-----
        if 'the time' in query:
            hour = datetime.datetime.now().strftime('%H')
            min = datetime.datetime.now().strftime('%M')
            say(f'the time is {hour} {min}')
        #-----apps-----
        if'open chrome' in query.lower():
            chrome_path=r"C:\Program Files\Google\Chrome\Application\chrome.exe"
            subprocess.Popen([chrome_path])
        #-----openai-----

        #say(query)
