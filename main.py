import pyaudio
import speech_recognition as s_r
import keyboard  # using module keyboard
import pandas as pd
import numpy
import sys
import Levenshtein as ls #https://rawgit.com/ztane/python-Levenshtein/master/docs/Levenshtein.html

#mircophone setup
# print(s_r.__version__)
s_r.Microphone.list_microphone_names()
# print(s_r.Microphone.list_microphone_names()) #print all the microphones connected to your machine
my_mic = s_r.Microphone(device_index=1)

r = s_r.Recognizer() #S_R constructor

WIT_AI_KEY = 'IQAXGNZQWIAZL5VAI7GUT6JK3P3RJ3TZ' #wit API key

#data logging arrays:
i = 0
j = 0
log_control = False
#   google
Transcript_google = []
google_l_distance = []
google_jaro = []
#   sphinx
Transcript_sphinx = []
sphinx_l_distance = []
sphinx_jaro = []
#   wit
Transcript_wit = []
wit_l_distance = []
wit_jaro = []
#manuscript
Manuscript = ["Can I please see the door to needle time for last quarter.", "The quick brown dog jumped over the lazy fox.", 'The purple buglar alarm.']

while True:
    if keyboard.is_pressed('q'):
        try:
            with my_mic as source:
                r.adjust_for_ambient_noise(my_mic, duration=0.2)
                print("Please talk into the microphone")
                audio = r.listen(source)
                Transcription_wit = r.recognize_wit(audio, key=WIT_AI_KEY)  # to print voice into text
                Transcription_google = r.recognize_google(audio)  # to print voice into text
                Transcription_sphinx = r.recognize_sphinx(audio)  # to print voice into text
                print('Google: '+Transcription_google+'\n' + 'sphinx: ' + Transcription_sphinx + '\n' + 'wit: '+ Transcription_wit)
                Transcript_google.append(Transcription_google)
                Transcript_sphinx.append(Transcription_sphinx)
                Transcript_wit.append(Transcription_wit)
                i += 1
                log_control = True

        except s_r.UnknownValueError:
            print("I did not catch that, can you please say it again")
            r = s_r.Recognizer()
            continue

        except s_r.RequestError as e:
            print("Could not request results from API; {0}".format(e))
            continue
    try:
        if keyboard.is_pressed('l'):
            if len(Manuscript) == len(Transcript_google):
                for j in range(len(Manuscript)):
                    # Levenshtein distance
                    google_l_distance.append(ls.distance(Manuscript[j], Transcript_google[j]))  #google
                    sphinx_l_distance.append(ls.distance(Manuscript[j], Transcript_sphinx[j]))  #sphinx
                    wit_l_distance.append(ls.distance(Manuscript[j], Transcript_wit[j])) #wit
                    # jaro_winkler
                    google_jaro.append(ls.jaro(Manuscript[j], Transcript_google[j])) #google
                    sphinx_jaro.append(ls.jaro(Manuscript[j], Transcript_sphinx[j])) #sphinx
                    wit_jaro.append(ls.jaro(Manuscript[j], Transcript_wit[j])) #wit
                    j += 1
                dict = {'Manuscript': Manuscript, 'Google': Transcript_google, 'Sphinx': Transcript_sphinx, 'Wit.ai': Transcript_wit,
                    'Google distance': google_l_distance, 'Google string': google_jaro, 'Sphinx distance': sphinx_l_distance,
                    'Sphinx string': sphinx_jaro, 'Wit.ai distance': wit_l_distance, 'Wit.ai string': wit_jaro}
            else:
                dict = {'Google': Transcript_google, 'Sphinx': Transcript_sphinx,
                    'Wit.ai': Transcription_wit}

            if log_control:
                print(wit_jaro)
                df = pd.DataFrame(dict)
                df.to_csv('Transcriptions.csv')
                print("Logging complete")
                log_control = False
    except Exception as e:
        continue
