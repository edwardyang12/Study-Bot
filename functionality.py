import pyaudio,os
import speech_recognition as sr
def mainfunction(source):
    audio = r.listen(source)
    user = r.recognize_google(audio)
    print(user)
    if user == "hello":
        print("you said hello")

if __name__ == "__main__":
    r = sr.Recognizer()
    with sr.Microphone() as source:
        while 1:
            mainfunction(source)
