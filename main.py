import pyaudio
import speech_recognition as s_r
import keyboard  # using module keyboard
import pandas as pd

#google
#print(s_r.__version__)
s_r.Microphone.list_microphone_names()
#print(s_r.Microphone.list_microphone_names()) #print all the microphones connected to your machine
my_mic = s_r.Microphone(device_index=1)

r = s_r.Recognizer()


i = 0

Transcript = []
Manuscript = ["Hello my name Karl and I like nuts", "The quick brown dog jumped over the lazy fox", 'The purple buglar alarm']


while True:
    if keyboard.is_pressed('q'):
        try:
            with my_mic as source:
                r.adjust_for_ambient_noise(my_mic, duration=0.2)
                print("Please talk into the microphone")
                audio = r.listen(source)
                Transcription = r.recognize_google(audio)  # to print voice into text
                print(Transcription)
                Transcript.append(Transcription)
                dict = {'Transcript': Transcript}
                df = pd.DataFrame(dict)
                i += 1
                df.to_csv('Transcriptions.csv')
        except r.UnknownValueError():

            r = s_r.Recognizer()
            continue
