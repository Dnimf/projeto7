from filtros import *
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import butter, iirnotch
import sounddevice as sd
import control as ctrl
from scipy.signal import freqz, lfilter

from FFTP7 import *
bandas = [
    20, 32, 64,
    125, 250, 500,
    1e3, 2e3, 4e3,
    8e3, 16e3, 20e3
]
# gravacao
T = 5
fs = 48000
# fs = 441000
gain_db = 0
numAmostras = int(fs*T)
t = np.linspace(0, T, numAmostras, endpoint=False)
audio = sd.rec(int(numAmostras), fs, channels=1)
sd.wait()
audioUnico=[]
for i in audio:
    audioUnico.append(i[0])
# cria equacao
magnitudes = np.arange(start=-10, stop=12, step=2)
print(bandas)
f0 = int(input("Banda da frequencia (Hz): "))
Q = descobreQ(f0)
gain_db = float(input("Ganho em dB: "))
b, a = peaking_eq(f0, gain_db, Q, fs)
G1= ctrl.TransferFunction(b,a, dt=(1/fs))
adiciona = input("deseja colocar mais?")
if adiciona=="y":
    while True:
        f0 = int(input("Banda da frequencia (Hz): "))
        if  f0 == 0:
            break
        Q = descobreQ(f0)
        
        gain_db = float(input("Ganho em dB: "))
        b, a = peaking_eq(f0, gain_db, Q, fs)
        G2= ctrl.TransferFunction(b,a, dt=(1/fs))
        G1 = ctrl.series(G1,G2)
print(G1)
ganhos = ctrl.tfdata(G1)
b1 = ganhos[0][0][0]
a1 = ganhos[1][0][0]
b=[]
a=[]
for i in b1:
    b.append(float(i))
for j in a1:
    a.append(float(j))
print(audio[0],audio[1])
audio_tratado = trata_audio(audioUnico, b, a)
print()
print(len(a))
sd.play(audio_tratado,fs)
sd.wait()
freqs, magnitude, magnitude_db = compute_fft(audioUnico, fs, window=None, nfft=None, return_complex=False)
plot_time_and_spectrum(t, audioUnico, fs , freqs, magnitude, magnitude_db, x_label_time='Tempo (s)')
plot_filter_response(ganhos[0][0][0],ganhos[1][0][0],fs)
freqs, magnitude, magnitude_db = compute_fft(audio_tratado, fs, window=None, nfft=None, return_complex=False)
plot_time_and_spectrum(t, audio_tratado, fs , freqs, magnitude, magnitude_db, x_label_time='Tempo (s)')
plt.show()
print("Saiu do loop")



