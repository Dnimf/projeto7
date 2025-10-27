from filtros import *
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import butter, iirnotch
import sounddevice as sd

bandas = [
    20, 32, 64,
    125, 250, 500,
    1e3, 2e3, 4e3,
    8e3, 16e3, 20e3
]
# gravacao
T = 2
fs = 44100
gain_db = 0
Q = 1
numAmostras = fs*T
audio = sd.rec(int(numAmostras), fs, channels=1)
sd.wait()
# cria equacao
magnitudes = np.arange(start=-10, stop=12, step=2)

while True:
    f0 = int(input("Banda da frequencia (Hz): "))
    if not f0:
        break
    gain_db = float(input("Ganho em dB: "))
    Q = 1
    b, a = peaking_eq(f0, gain_db, Q, fs)

print("Saiu do loop")