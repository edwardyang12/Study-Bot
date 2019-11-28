import random
import speech_recognition as sr
import voice
import text2number
import motor

r = sr.Recognizer()
derek = sr.AudioFile('output1.wav')

options = ["forward", "backward" , "rotateL", "rotateR"]
steps = []


def randomMove():
    for i in range(random.randrange(10)):
        amount = random.randrange(5)
        direction = random.choice(options)
        if(direction =='forward'):
            motor.forwardMove(amount)
        elif(direction == 'backward'):
            motor.backwardMove(amount)
        elif(direction == 'rotateL'):
            motor.rotate90left(5)
        else:
            motor.rotate90right(5)
        steps.insert(0,direction +" " + amount)
    
def retrace():
    for i in steps:
        if("forward" in i):
            i = i[len("forward")+1 :]
            motor.backwardMove(int(i))
        elif("backward" in i):
            i = i[len("backward")+1 :]
            motor.forwardMove(int(i))
        elif("rotateL" in i):
            motor.rotate90rightt(5)
        else:
            motor.rotate90left(5)

def recognizeMove(audio):
    tryMove = (voice.instantListen(audio,r))['alternative'][0]['transcript']
    information = tryMove.split(" ")
    if(information[0]=='forward'):
        print('forward ' + str(text2number.magic(information[1])))
        motor.forwardMove(text2number.magic(information[1]))
        steps.insert(0,"forward " + text2number.magic(information[1]))
    elif(information[0] == 'backward'):
        print('backward ' + str(text2number.magic(information[1])))
        motor.backwardMove(text2number.magic(information[1]))
        steps.insert(0,"backward " + text2number.magic(information[1]))
    elif(information[0] == 'left'):
        print("rotate to left")
        motor.rotate90left(5)
        steps.insert(0,"rotateL")
    elif(information[0] == 'right'):
        print("rotate to right")
        motor.rotate90right(5)
        steps.insert(0,"rotateR")
    elif(information[0] == 'study'):
        motor.backwardMove(10)
        steps.insert(0,"backward 10")
        randomMove()
    elif(information[0] == 'back'):
        retrace()
    else:
        print("no movement")

randomMove()

