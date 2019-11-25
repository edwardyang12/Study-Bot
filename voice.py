import speech_recognition as sr
import record 
r = sr.Recognizer()

record.recorder(6)
derek = sr.AudioFile('output1.wav')

def instantListen(mic, r):
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    
    #print((r.recognize_google(audio,language = 'en-US', show_all=True))['alternative'][0]['transcript'])
    return r.recognize_google(audio,language = 'en-US', show_all=True)

instantListen(derek,r)

