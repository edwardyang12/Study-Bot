import random
import speech_recognition as sr
import voice
import text2number
import servomotor

r = sr.Recognizer()
derek = sr.AudioFile('output1.wav')

def regMove(direction,steps):
    move(steps)

def takePhone():
    pass


def recognizeMove(audio):
    tryMove = (voice.instantListen(audio,r))['alternative'][0]['transcript']
    information = tryMove.split(" ")
    if(information[0]=='forward'):
        print('forward ' + str(text2number.magic(information[1])))
    elif(information[0] == 'backward'):
        print('backward ' + str(text2number.magic(information[1])))
    elif(information[0] == 'left'):


recognizeMove(derek)
