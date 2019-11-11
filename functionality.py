import pyaudio,os
import speech_recognition as sr
import time
import datetime
def mainfunction(source):
    audio = r.listen(source)
    my_time  = r.recognize_google(audio)
    
    #Possible audio input strings
    timeStrings = ["one", "two", "three", "four", "five"]
    timeIntegerStrings = ["1", "2", "3", "4", "5"]

    #Times for timer as ints
    sleepTime = [1, 2, 3, 4, 5]
    counter = 0;

    #Sleep for the time specified
    while counter < len(timeStrings):
        if str(my_time) == timeStrings[counter] or str( my_time) == timeIntegerStrings[counter]:            
            print("Sleeping for " + timeStrings[counter] + " seconds")
            time.sleep(sleepTime[counter])
        counter = counter + 1    
    
    print("Done sleeping")

if __name__ == "__main__":
    r = sr.Recognizer()
    with sr.Microphone() as source:
        while 1:
            mainfunction(source)
