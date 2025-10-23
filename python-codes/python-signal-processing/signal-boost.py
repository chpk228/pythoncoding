import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

fs = 1000
t = np.linspace(0, 1, fs, endpoint=False)
f1 = 50
f2 = 120
amplitude1 = 0.7
amplitude2 = 0.3
noise_amplitude = 0.1

pure_signal = amplitude1 * np.sin(2 * np.pi * f1 * t) + amplitude2 * np.sin(2 * np.pi * f2 * t)
noise = noise_amplitude * np.random.randn(len(t))
noisy_signal = pure_signal + noise

N = len(noisy_signal)
yf = np.fft.fft(noisy_signal)
xf = np.fft.fftfreq(N, 1 / fs)

nyquist = 0.5 * fs
cutoff_freq = 70
normal_cutoff = cutoff_freq / nyquist
b, a = signal.butter(4, normal_cutoff, btype='low', analog=False)
filtered_signal = signal.filtfilt(b, a, noisy_signal)

plt.figure(figsize=(12, 6))

plt.subplot(3, 1, 1)
plt.plot(t, noisy_signal)
plt.title('Noisy Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.subplot(3, 1, 2)
plt.plot(xf, 2.0/N * np.abs(yf))
plt.title('Frequency Spectrum of Noisy Signal')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.xlim(0, fs / 2)

plt.subplot(3, 1, 3)
plt.plot(t, filtered_signal)
plt.title('Filtered Signal (Low-Pass)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()
