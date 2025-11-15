import numpy as np
import matplotlib.pyplot as plt

fs = 2000
t = np.linspace(0, 1, fs, endpoint=False)
x = np.sin(2*np.pi*50*t)

X = np.fft.fft(x)
freqs = np.fft.fftfreq(len(x), 1/fs)

plt.plot(freqs[:fs//2], np.abs(X)[:fs//2])
plt.show()

