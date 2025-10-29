import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz, lfilter

def peaking_eq(f0, gain_db, Q, fs):
    """
    Design a peaking EQ filter.
    
    Parameters:
        f0 : float      # center frequency in Hz
        gain_db : float # gain in dB (+boost, -cut)
        Q : float       # quality factor
        fs : float      # sampling rate in Hz
        
    Returns:
        b, a : filter coefficients
    """
    A = 10**(gain_db / 40)  # amplitude
    omega = 2 * np.pi * f0 / fs
    alpha = np.sin(omega) / (2 * Q)

    b0 = 1 + alpha * A
    b1 = -2 * np.cos(omega)
    b2 = 1 - alpha * A
    a0 = 1 + alpha / A
    a1 = -2 * np.cos(omega)
    a2 = 1 - alpha / A

    b = np.array([b0, b1, b2]) / a0
    a = np.array([a0, a1, a2]) / a0
    return b, a

def plot_filter_response(b, a, fs, title="Filter Response"):
    w, h = freqz(b, a, fs=fs)
    plt.figure(figsize=(8, 4))
    plt.plot(w, 20 * np.log10(abs(h)))
    plt.title(title)
    plt.xlabel('Frequency [Hz]')
    plt.ylabel('Gain [dB]')
    plt.grid()
    plt.ylim(-15, 15)
    # plt.show()
def descobreQ(f):
    bandas = [
    20, 32, 64,
    125, 250, 500,
    1e3, 2e3, 4e3,
    8e3, 16e3, 20e3
]
    if f<=bandas[0]:
        q=0.1
    elif f<=bandas[1]:
        q=0.5
    elif f<=bandas[2]:
        q=0.85
    elif f<=bandas[3]:
        q=2.5
    elif f<=bandas[4]:
        q=3.75
    elif f<=bandas[5]:
        q=6.5
    elif f<=bandas[6]:
        q=14
    elif f<=bandas[7]:
        q=18
    elif f<=bandas[8]:
        q=55
    elif f<=bandas[9]:
        q=55
    elif f<=bandas[10]:
        q=40
    elif f<=bandas[11]:
        q=10
    return q
def trata_audio(audio,b, a):
    tone = []
    for t1 in range(len(audio)):
        t2=float(audio[t1])
        if t2 == 0:
            t2=float(0.0001)
        tone.append(t2)
    y=[tone[0],tone[1]]
    print(y)
    print(audio[0],audio[1])
    # k=2
    # while k<len(tone):
    #     lista=[y[k-1],y[k-2],tone[k],tone[k-1],tone[k-2]]
    #     yk= b[0]*y[k-1] + b[1]*y[k-2] + b[2] + a[0]*tone[k] + a[1]*tone[k-1] +a[2]*tone[k-2]
    #     # print(tone[k])
    #     if float(0) in lista:
    #         yk=tone[k]
    #     y.append(yk)
    #     k+=1
    # ynp = np.array(y)
    ynp = lfilter(b,a,tone)
    return ynp
if __name__ == "__main__":
    # Parameters
    fs = 44100         # Sampling rate (Hz)
    f0 = 1000          # Center frequency (Hz)
    gain_db = -6        # Gain in dB
    Q = 1.0            # Quality factor

    # Design and plot
    b, a = peaking_eq(f0, gain_db, Q, fs)
    plot_filter_response(b, a, fs, f"Peaking EQ at {f0} Hz, Gain = {gain_db} dB")
