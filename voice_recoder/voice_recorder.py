# import required libraries 
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

# sampling frequence
freq = 44100

# recording durtion
duration = 5

# start recorder with the given values
# of duration ans sample frequency
recording = sd.rec(int(duration * freq), samplerate = freq, channels = 2)

# record audio for the given number of seconds
sd.wait()

# This will convert the NumPy array to an audio
# file with the given sampling frequency
write("recording0.wav", freq, recording)

# file with the given sampling frequency
wv.write("recording1.wav", recording, freq, sampwidth = 2)