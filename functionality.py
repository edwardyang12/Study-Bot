import pyaudio,os
import speech_recognition as sr
import time
import datetime
def mainfunction(source):
    audio = r.listen(source)
    my_time  = r.recognize_google(audio)
    
    #Possible audio input strings
    time_strings = ["one", "two", "three", "four", "five"]
    time_integer_strings = ["1", "2", "3", "4", "5"]

    #Times for timer as ints
    sleep_time = [1, 2, 3, 4, 5]
    counter = 0;

    #Sleep for the time specified
    while counter < len(time_strings):
        if str(my_time) == time_strings[counter] or str(my_time) == time_integer_strings[counter]:            
            print("Sleeping for " + time_strings[counter] + " seconds")
            time.sleep(sleep_time[counter])
        counter = counter + 1    
    
    print("Done sleeping")

if __name__ == "__main__":
    r = sr.Recognizer()
    with sr.Microphone() as source:
        while 1:
            mainfunction(source)
