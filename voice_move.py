import random
import speech_recognition as sr
import voice
r = sr.Recognizer()
derek = sr.AudioFile('output1.wav')
def regMove(steps):
    pass

def takePhone():
    pass


def recognizeMove(audio):
    tryMove = (voice.instantListen(audio,r))['alternative'][0]['transcript']
    information = tryMove.split(" ")
    if(information[0]=='forward'):
        print('forward' + information[1])

recognizeMove(derek)
