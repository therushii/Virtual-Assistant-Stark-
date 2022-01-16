import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import webbrowser
import requests

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

def wishme():
    hour = datetime.datetime.now().hour
    if hour >= 4 and hour <12:
        talk("Hello vary good morning sir!")
        print("Hello vary good morning sir!")

    if hour >12 and hour <17:
        talk("Hello vary good afternoon sir!")
        print("Hello vary good afternoon sir!")

    if hour >17 and hour <2:
        talk("Hello vary good evening sir!")
        print("Hello vary good evening sir!")
wishme()


def take_command():

    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)
    except:
        pass
    return command
def run_stark():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    if 'who are you' in command:
        talk('hello i am stark and i am your virtual assistant')
        print('hello i am stark and i am your virtual assistant')
    if 'which is best virtual assistant' in command:

        talk('ha ha ha as you know i am the best !!')
        print('ha ha ha as you know i am the best !!')
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
        print(time)
    if 'tell me' in command:

        person = command.replace('tell me', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    if 'open youtube' in command:
        talk("Here you go to Youtube")
        print("Here you go to Youtube")
        webbrowser.open("youtube.com")
    if'open netflix' in command:
        talk("Here you go to netflix")
        print("Here you go to netflix")
        webbrowser.open("netflix.com")
    if 'open amazon' in command:
        talk("Here you go to amazon")
        print("Here you go to amazon")
        webbrowser.open("amazon.com")
    if 'show me mail' in command:
        talk('showing you mails')
        print('showing you mails')
        webbrowser.open("gmail.com")
    if 'open google earth' in command:
        talk("Here you go to google earth")
        print("Here you go to google earth")
        webbrowser.open('earth.google.com')
    if 'weather' in command:
        city = "mumbai"
        res = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=16f0afad2fd9e18b7aee9582e8ce650b&units=metric").json()
        temp1 = res["weather"][0]["description"]
        temp2 = res["main"]["temp"]
        talk(f"Temperature is {format(temp2)} degree Celsius \nWeather is {format(temp1)}")
        print(f"Temperature is {format(temp2)} degree Celsius \nWeather is {format(temp1)}")
    else:
        print('sorry can you say it again')

while True:
    run_stark()