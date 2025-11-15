import numpy as np
import matplotlib.pyplot as plt

fs = 1000
t = np.linspace(0, 1, fs, endpoint=False)
x = np.sin(2*np.pi*50*t) + 0.5*np.sin(2*np.pi*120*t)

plt.plot(t, x)
plt.show()

