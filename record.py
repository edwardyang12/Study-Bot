import pyaudio
import wave
from os import path


chunk = 1024  # Record in chunks of 1024 samples
sample_format = pyaudio.paInt16  # 16 bits per sample
channels = 2
fs = 44100  # Record at 44100 samples per second
tempname = "output1"

def writeFile(tempname):
    counter = 1
    while(path.exists(tempname+".wav")):
       counter = counter + 1
       tempname = tempname[0:len(tempname)-1] + str(counter)
    return tempname[0:len(tempname)-1] + str(counter) + ".wav"

def recorder(seconds):
    p = pyaudio.PyAudio() 

    print('Recording')

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []  # Initialize array to store frames

    # Store data in chunks for 3 seconds
    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)

    # Stop and close the stream 
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()

    print('Finished recording')

    # Save the recorded data as a WAV file
    wf = wave.open(writeFile(tempname), 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()
    
while(True):
    recorder(5)
