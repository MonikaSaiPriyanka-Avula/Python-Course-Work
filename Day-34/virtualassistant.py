#pip install SpeechRecognition
#Pip install pyttsx3

import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wikipedia
#----------------------------
#Speak Function
#----------------------------
def speak(text):
    engine=pyttsx3.init()
    voices=engine.getProperty("voices")
    engine.setProperty("voice",voices[0].id)
    engine.setProperty("rate",170)
    engine.setProperty("volume",1.0)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

#-------------------------
#Listen Function
#-------------------------
def listen():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.........")
        recognizer.pause_threshold=1
        audio=recognizer.listen(source)
        print("Audio Done")
    try:
        command=recognizer.recognize_google(audio,language="en-in")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't understand.")
        return ""
    except sr.RequestError:
        speak("Speech service is unavailable.")
        return ""
    
#----------------------
#Process Command
#----------------------
speak("Hello I'm your Voice Assistant. How can I help you?")
while True:
    command=listen()
    if "time" in command:
        cuurent_time=datetime.datetime.now().strftime("%I:%M:%p")
        speak(f"The current time is {cuurent_time}")
    elif "date" in command:
        today=datetime.datetime.now().strftime("%d %B %Y")
        speak(f"Today's date is {today}")
    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif "open youtube" in command:
        speak("Opening Youtube")
        webbrowser.open("https://www.youtube.com")
    elif "open gamil" in command:
        speak("Opening Gmail")
        webbrowser.open("https://www.gmail.com")
    elif "open chat gpt" in command:
        speak("Opening Chat gpt")
        webbrowser.open("https://www.chatgpt.com")
    elif "your name" in command:
        speak("My name is Nova. I am your Voice Assistant")
    elif "hello" in command:
        speak("Hello.How can I help you today.")
    elif "who created you" in command:
        speak("I was created using python.")
    elif "bye" in command or "exit" in command:
        speak("Goodbye.Have a great day!!")
        break
    else:
        speak("Sorry.I do not know that command yet")