import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour==0 and hour==12:
        speak("Good morning!")
    elif hour==12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("good evening!")

    speak(" I am your friend Mr Paras. how may I help you")            

def takeCommand():
   # it take voice input and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold =1
        audio = r.listen(source)

    try:
        print("Recogising...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: \n {query}")

    except Exception:

        print("say that again please...")
        return "None"        
    return query
if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching wikipedia....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
            print(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
 
        elif 'exit' in query:
            break
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'play music' in query:
            music_dir = 'C:\\Users\\paras goel\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))    

             