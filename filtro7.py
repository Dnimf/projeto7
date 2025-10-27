from filtros import *
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import butter, iirnotch
import sounddevice as sd
import control as ctrl
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
numAmostras = fs*T
# audio = sd.rec(int(numAmostras), fs, channels=1)
# sd.wait()
# cria equacao


def descobreQ(f):
    bandas = [
    20, 32, 64,
    125, 250, 500,
    1e3, 2e3, 4e3,
    8e3, 16e3, 20e3
]
    if f<bandas[0]:
        q=1
    elif f<bandas[1]:
        q=2
    elif f<bandas[3]:
        q=3
    elif f<bandas[4]:
        q=4
    elif f<bandas[5]:
        q=5
    elif f<bandas[6]:
        q=6
    elif f<bandas[7]:
        q=7
    elif f<bandas[8]:
        q=8
    elif f<bandas[9]:
        q=9
    elif f<bandas[10]:
        q=10
    elif f<=bandas[11]:
        q=11
    return q

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
print(f"ganhos {ganhos}")
print(ganhos[0][0][0],ganhos[1][0][0])
plot_filter_response(ganhos[0][0][0],ganhos[1][0][0],fs)
print("Saiu do loop")



