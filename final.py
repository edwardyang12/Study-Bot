import record
import voice_move
import voice
import speech_recognition as sr
import pygame

r = sr.Recognizer()

tempfile = "output1"
counter =1

def newFile(tempfile):
    counter = counter + 1
    tempfile = tempfile[0:len(tempname)-1] + str(counter)
    return tempfile[0:len(tempfile)-1] + str(counter) + ".wav"

if __name__ == "__main__":
    while(True):
        record.recorder(6)
        analyze = sr.AudioFile(newFile(tempfile))
        move = voice_recognizeMove(analyze)
        if(move):
            pygame.init()
            sound = pygame.mixer.Sound("alert.wav")
            sound.play()
            time.sleep(2)
            sound.stop()
        sleep = voice_move.recognizeSleep(analyze)
        if(sleep):
            pygame.init()
            sound = pygame.mixer.Sound("alert.wav")
            sound.play()
            time.sleep(2)
            sound.stop()
