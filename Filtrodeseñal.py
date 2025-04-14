import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

# Simulación de señal EMG con ruido
fs = 1000  # Frecuencia de muestreo
t = np.linspace(0, 1, fs)
emg_raw = np.sin(2*np.pi*50*t) + 0.5*np.random.randn(len(t))

# Filtro pasa banda (20–450 Hz)
def filtro_emg(signal):
    nyq = 0.5 * fs
    b, a = butter(4, [20/nyq, 450/nyq], btype='band')
    return filtfilt(b, a, signal)

emg_filtrada = filtro_emg(emg_raw)
umbral = 0.5
activacion = np.any(np.abs(emg_filtrada) > umbral)

# Mostrar resultados
plt.plot(t, emg_raw, label='EMG cruda')
plt.plot(t, emg_filtrada, label='EMG filtrada')
plt.axhline(umbral, color='r', linestyle='--', label='Umbral')
plt.legend()
plt.title("Filtrado y detección de señal EMG")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.show()

print("¿Activación muscular?:", activacion)
