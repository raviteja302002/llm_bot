import speech_recognition as sr
import pyttsx3
import google.generativeai as genai
import sys


recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

genai.configure(api_key="AIzaSyB3_i2ehLE99CvMITbbVaHzf3FWJQq8ykk")
model=genai.GenerativeModel("gemini-1.5-flash")


def recognize_speech():
    with sr.Microphone() as source:
        print("Listening...")
        
        speak("Listening...")
        try:
           
            recognizer.adjust_for_ambient_noise(source,duration=1)
            audio = recognizer.listen(source, timeout=5)
            
            
            text = recognizer.recognize_google(audio)
            # text=text.replace('*','')
            if text in ['exit','leave']:
                speak("exiting")
                print("exiting")
                sys.exit(0)

            print(f"You said: {text}")
            
            
            response = f"You said: {text}"
            speak(response)
            
            responsem=model.generate_content(text)
            print(responsem.text)
            speak(responsem.text)
            
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
            speak("Sorry, I could not understand the audio.")
        except sr.RequestError:
            print("Could not request results; please check your internet connection.")
            speak("Could not request results; please check your internet connection.")


while True:
    recognize_speech()
