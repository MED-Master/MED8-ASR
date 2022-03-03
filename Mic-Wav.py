from deepspeech import Model
import numpy as np
import os
import pyaudio
import wave

# Record in chunks of 1024 samples
chunk = 1024

# 16 bits per sample
sample_format = pyaudio.paInt16
chanels = 1

# Record at 44400 samples per second
smpl_rt = 44400
seconds = 4
filename = "audioInput.wav"

# Create an interface to PortAudio
pa = pyaudio.PyAudio()

stream = pa.open(format=sample_format, channels=chanels,
                 rate=smpl_rt, input=True,
                 frames_per_buffer=chunk)

print('Recording...')

# Initialize array that be used for storing frames
frames = []

# Store data in chunks for 8 seconds
for i in range(0, int(smpl_rt / chunk * seconds)):
    data = stream.read(chunk)
    frames.append(data)

# Stop and close the stream
stream.stop_stream()
stream.close()

# Terminate - PortAudio interface
pa.terminate()

print('Done !!! ')

# Save the recorded data in a .wav format
sf = wave.open(filename, 'wb')
sf.setnchannels(chanels)
sf.setsampwidth(pa.get_sample_size(sample_format))
sf.setframerate(smpl_rt)
sf.writeframes(b''.join(frames))
sf.close()



os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

modelPath = 'deepspeech-0.9.3-models.pbmm'
scorerPath = 'deepspeech-0.9.3-models.scorer'
audioPath = 'audioInput.wav'

ds = Model(modelPath)
ds.enableExternalScorer(scorerPath)

fin = wave.open(audioPath, 'rb')
frames = fin.readframes(fin.getnframes())
audio = np.frombuffer(frames, np.int16)
text = ds.stt(audio)

print(text)