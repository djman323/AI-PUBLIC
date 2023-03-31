import speech_recognition as sr
import pyttsx3
import pywhatkit as kt
import datetime
import wikipedia
import pyjokes
import webbrowser
import pyautogui
import os
import openai

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice, language='en-in')
            command = command.lower()
            if 'edith' in command:
                command = command.replace('edith', '')
                print(command)
    except:
        pass
    return command

def run_edith():

        command = take_command()
        print(command)

        if 'play' in command:
            song = command.replace('play', '')
            print(song)
            talk('playing ' + song)
            kt.playonyt(song)

        elif 'hello' in command:
            talk('hello sir')
            talk('What can I do for you?')

        elif 'message to mummy' in command:
            msg = command.replace('message to mummy', 'hi')
            kt.sendwhatmsg_instantly("+916351389332", "",)

        elif 'message to pops' in command:
            msg1 = command.replace('message to pops', 'hi')
            kt.sendwhatmsg_instantly("+919925000488", "",)

        elif 'message to aarav' in command:
            msg1 = command.replace('message to aarav', 'hi')
            kt.sendwhatmsg_instantly("+919978923710", "",)

        elif 'notepad' in command:
            os.startfile('%windir%\system32\notepad.exe')

        elif 'search' in command:
            google = command.replace('search', '')
            print(google)
            talk('searching ' + google)
            kt.search(google)
            talk('here it is sir')

        elif 'website' in command:
            command = command.replace('edith', '')
            talk('ok sir, launching...')
            command = command.replace("website", "")
            web1 = command.replace('open', "")
            web2 = command.replace('https//www.' + web1 + '.com')
            webbrowser.open(web2)
            talk('launching...')

        elif 'launch' in command:
            talk('tell me the name of the website')
            name = take_command()
            web3 = ('https//www.' + name + '.com')
            webbrowser.open(web2)
            talk('ok sir, launching...')

        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time)
            kt.say(time)

        elif 'who is' in command:
            person = command.replace('who is', '')
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)

        elif 'youtube search' in command:
            talk("here, is what I found for your search")
            yt = command.replace('edith', '')
            yt = command.replace('youtube search', '')
            web = 'https://www.youtube.com/results?search_query=' + command
            webbrowser.open(web)
            talk('here it is')

        elif 'are you single' in command:
            talk('I am in a relationship with wifi')

        elif 'joke' in command:
             talk(pyjokes.get_joke())

        elif 'bye' in command:
            talk('ok sir, have a great day bye!')
            exit

        else:
            talk('Please say the command again.')

while True:
    run_edith()
