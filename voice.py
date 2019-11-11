import speech_recognition as sr
import record 
r = sr.Recognizer()

record.recorder(5)
derek = sr.AudioFile('output.wav')

def instantListen(mic, r):
    
    with mic as source:
        audio = r.listen(source)
    print(r.recognize_google(audio,language = 'en-US'))

instantListen(derek,r)

