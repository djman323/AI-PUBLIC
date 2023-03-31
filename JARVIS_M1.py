import speech_recognition as sr
import pyttsx3
import pywhatkit as kt
import datetime
import wikipedia
import pyjokes
import os

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
                print(command)
    except:
        pass
    return command


def run_jarvis():

    command = take_command()
    print(command)

    if 'play' in command:
        song = command.replace('play', '')
        print(song)
        talk('playing ' + song)
        kt.playonyt(song)

    elif 'notepad' in command:
        os.startfile('%windir%\system32\notepad.exe')

    elif 'search' in command:
        google = command.replace('search', '')
        print(google)
        talk('searching ' + google)
        kt.search(google)

    elif 'message to mummy' in command:
        msg = command.replace('message to mummy', 'hi')
        kt.sendwhatmsg_instantly("+916351389332", "",)

    elif 'message to pops' in command:
        msg1 = command.replace('message to pops', 'hi')
        kt.sendwhatmsg_instantly("+919925000488", "",)

    elif 'message to aarav' in command:
        msg1 = command.replace('message to aarav', 'hi')
        kt.sendwhatmsg_instantly("+919978923710", "",)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
        kt.say(time)

    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'open chatgpt' in command:
        google = command.replace('open', '')
        print(google)
        talk('searching' + google)
        kt.search(google)

    elif 'weather' in command:
        weather = command.replace('weather', '')
        print(weather)
        talk('Current weather is' + weather)
        kt.weather(weather)

    elif 'date' in command:
        talk('sorry, I have a headache')

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
    run_jarvis()
