import serial
import time
import numpy as np
from scipy.signal import butter, filtfilt

# Configura conexión serial
arduino = serial.Serial('COM3', 9600)
time.sleep(2)

# Señal simulada EMG
fs = 1000
t = np.linspace(0, 1, fs)
emg = np.sin(2*np.pi*60*t) + np.random.randn(len(t))*0.5

# Filtrado
def filtro_emg(signal):
    nyq = 0.5 * fs
    b, a = butter(4, [20/nyq, 450/nyq], btype='band')
    return filtfilt(b, a, signal)

emg_filtrada = filtro_emg(emg)
umbral = 0.5

# Enviar señal a Arduino
if np.any(np.abs(emg_filtrada) > umbral):
    arduino.write(b'1')
    print("EMG activada: señal enviada al servomotor")
else:
    print("Sin activación EMG")

arduino.close()
