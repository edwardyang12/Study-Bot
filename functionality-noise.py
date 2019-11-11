import pyaudio,os
import speech_recognition as sr
import pygame

def mainfunction(source):
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
    user = r.recognize_google(audio)
    print(user)
    if user == "hello":
        print("you said hello")
        #Plays music if input is "hello"
        pygame.init()
        sound = pygame.mixer.Sound("alert.wav")
        sound.play()
        pygame.event.wait() #Music continues until a key is pressed

if __name__ == "__main__":
    r = sr.Recognizer()
    with sr.Microphone() as source:
        while 1:
            mainfunction(source)

