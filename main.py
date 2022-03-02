import pyaudio
import speech_recognition as s_r
import keyboard  # using module keyboard
import pandas as pd
import vosk

# google
# print(s_r.__version__)
s_r.Microphone.list_microphone_names()
# print(s_r.Microphone.list_microphone_names()) #print all the microphones connected to your machine
my_mic = s_r.Microphone(device_index=1)

r = s_r.Recognizer()


i = 0
WIT_AI_KEY = '45VKV53C2GSH4CKFOJSO76SYQ3JD7YTF'
Transcript_google = []
Transcript_sphinx = []
Transcript_wit = []
Manuscript = ["Hello my name Karl and I like nuts", "The quick brown dog jumped over the lazy fox",
              'The purple buglar alarm']

while True:
    if keyboard.is_pressed('q'):
        try:
            with my_mic as source:
                r.adjust_for_ambient_noise(my_mic, duration=0.2)
                print("Please talk into the microphone")
                audio = r.listen(source)
                Transcription_google = r.recognize_google(audio)  # to print voice into text
                Transcription_sphinx = r.recognize_sphinx(audio)  # to print voice into text
                Transcription_wit = r.recognize_wit(audio, key=WIT_AI_KEY)  # to print voice into text
                print('Google: '+Transcription_google+'\n' + 'sphinx: ' + Transcription_sphinx + '\n' + 'wit: '+ Transcription_wit)
                Transcript_google.append(Transcription_google)
                Transcript_sphinx.append(Transcription_sphinx)
                Transcript_wit.append(Transcription_wit)
                dict = {'google': Transcript_google, 'sphinx': Transcript_sphinx, 'wit': Transcription_wit}
                df = pd.DataFrame(dict)
                i += 1
                df.to_csv('Transcriptions.csv')
        except s_r.UnknownValueError:
            print("I did not catch that, can you please say it again")
            r = s_r.Recognizer()
            continue

        except s_r.RequestError as e:
            print("Could not request results from API; {0}".format(e))
            continue


