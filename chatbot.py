import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty("rate",150)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good morning!")
    elif hour>12 and hour<=18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am chatbot sir, please tell me how can i help you")
    print("Want anything like:\n "+ "Open(Youtube,Facebbok,Google)" + " Or can tell (day date and time)")
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please....")
        return "None"
    return query
if __name__ == "__main__":
    wishMe()
    while True:
        query = takecommand().lower()
        if 'how are you' in query:
            speak("i am fine what about you")
            reply = takecommand().lower()
            if "i am" in reply:
                speak("Okay")
        elif 'create' in query:
            speak("nikita agarwal")
        elif "youtube" in query:
            webbrowser.open("YouTube.com")
        elif "google" in query:
            webbrowser.open("google.com")
        elif "facebook" in query:
            webbrowser.open("facebook.com")
        elif "date" in query:
            cd = str(datetime.datetime.now().strftime("%B %D %Y"))
            engine.setProperty("rate", 150)
            speak(cd)
        elif "day" in query: 
            cd = str(datetime.datetime.now().strftime("%A"))
            engine.setProperty("rate", 150)
            speak(cd)
        elif "time" in query:
            speak(datetime.datetime.now().strftime("%H:%M:%S"))
        else:
            speak("Do you want to ask more?")
            ans=takecommand().lower()
            if "no" in ans:
                quit()

        