import speech_recognition as sr
import record 
r = sr.Recognizer()

record.recorder(5)
derek = sr.AudioFile('output1.wav')
ambient = sr.AudioFile('ambient.wav')
def instantListen(mic, r,ambient):
    r.adjust_for_ambient_noise(ambient)
    with mic as source:
        audio = r.listen(source)
    print(r.recognize_google(audio,language = 'en-US', show_all=True))

instantListen(derek,r,ambient)

