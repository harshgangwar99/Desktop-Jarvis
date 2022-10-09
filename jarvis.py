import datetime
import webbrowser
import pyttsx3
import speech_recognition as sr
import os
import wikipedia
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Zira Sir, Please tell me how may i help you")

def takeCommand():

   # it takes microphhone input from user

    r = sr.Recognizer() # calling a pre-function Recognizer

    with sr.Microphone() as source:         #To use microphone as source
        print("Listening.......")
        r.pause_threshold = 1
        audio = r.listen(source,0,3)

    try:
        print("Recogniting....")
        query = r.recognize_google(audio,language="en-in")
        print(f"You Said : {query}")

    except sr.UnknownValueError:

        r = sr.Recognizer()
        speak("I did not Understand you!! Please Try again!!")
        return takeCommand()
    query = str(query)
    return query.lower()

def sendEmail(to, content):
            server = smtplib.SMTP('smtp.gmail.com',587)
            server.ehlo()
            server.startls()
            server.login('youremail@gmail.com', 'your-password')
            server.sendmail('youremail@gmail.com', to, content)
            server.close()
wishMe()
if __name__ == "__main__":
    while True:

        query = takeCommand()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=1)
            speak("Accordig to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            
        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open twitter' in query:
            webbrowser.open("twitter.com")

        elif 'open gmail' in query:
            webbrowser.open("email.com")

        elif 'play music' in query:
            music_dir = DeprecationWarning
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        # elif 'open code' in query:
        #     codePath=

        elif 'email to vishal' in query:
            try:
                speak("what should I say?")
                content = takeCommand()
                to="vishalyourgmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend vishal bhai. I am not able to send this email")
                        


        