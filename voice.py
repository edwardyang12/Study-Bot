import speech_recognition as sr
import record
import time
r = sr.Recognizer()

#record.recorder(6)
#derek = sr.AudioFile('output1.wav')

def instantListen(mic, r):
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    
    #print((r.recognize_google(audio,language = 'en-US', show_all=True))['alternative'][0]['transcript'])
    return r.recognize_google(audio,language = 'en-US')

#instantListen(derek,r)

def recognizeSleep(audio):
    detected = False
    time = 0
    trySleep = instantListen(audio,r)
    information = trySleep.split(" ")
    if(information[0] == 'sleep'):
        print("sleeping for " + information[1] + information[2])
        if(information[2]=='minutes'):
            while time<text2number.magic(information[1])*60:
                print("slept for " + time + "seconds")
                time = time + 1
        elif(information[2] == 'hours'):
             while time<text2number.magic(information[1])*3600:
                print("slept for " + time + "seconds")
                time = time + 1
        elif(information[2] == "seconds"):
            while time<text2number.magic(information[1]):
                print("slept for " + time + "seconds")
                time = time + 1
        detected = True
    else:
        print("Finished")
    return detected
        
