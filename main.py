import pyaudio
import speech_recognition as s_r
import keyboard  # using module keyboard
import pandas as pd

#print(s_r.__version__)
s_r.Microphone.list_microphone_names()
print(s_r.Microphone.list_microphone_names()) #print all the microphones connected to your machine
my_mic = s_r.Microphone(device_index=1)

r = s_r.Recognizer()

#with my_mic as source:
#    print("Say now!!!!")
#    audio = r.listen(source)
#print(r.recognize_google(audio)) #to print voice into text

i = 0

Transcript = []
Manuscript = ["Hello my name Karl and I like nuts", "The quick brown dog jumped over the lazy fox", 'The purple buglar alarm']


while True:
    if keyboard.is_pressed('q'):
        with my_mic as source:
            print("Please talk into the microphone")
            audio = r.listen(source)
            Transcription = r.recognize_google(audio)  # to print voice into text
            print(Transcription)
            Transcript.append(Transcription)
            dict = {'Transcript': Transcript}
            df = pd.DataFrame(dict)
            i += 1
            df.to_csv('Transcriptions.csv')