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
#v_r = s_r.Recognizer_instance
#s_r.Recognizer(vosk.recognizer_instance.recognize_vosk)

i = 0
WIT_AI_KEY = '632718101326770'
Transcript = []
Manuscript = ["Hello my name Karl and I like nuts", "The quick brown dog jumped over the lazy fox",
              'The purple buglar alarm']

while True:
    if keyboard.is_pressed('q'):
        try:
            with my_mic as source:
                r.adjust_for_ambient_noise(my_mic, duration=0.2)
                print("Please talk into the microphone")
                audio = r.listen(source)
                Transcription = r.recognize_sphinx(audio)  # to print voice into text
                print(Transcription)
                Transcript.append(Transcription)
                dict = {'Transcript': Transcript}
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


