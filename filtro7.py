from  filtros import *
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import butter, iirnotch

bandas = [
    20, 32, 64,
    125, 250, 500,
    1e3, 2e3, 4e3,
    8e3, 16e3, 20e3
]

magnitudes = np.arange(start=-10, stop=12, step=2)
print(magnitudes)
