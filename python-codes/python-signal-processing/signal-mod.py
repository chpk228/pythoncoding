import numpy as np
import matplotlib.pyplot as plt

def create_signals(t, carrier_freq, message_freq, amplitude_carrier, amplitude_message, modulation_index):
    message_signal = amplitude_message * np.cos(2 * np.pi * message_freq * t)
    carrier_wave = amplitude_carrier * np.cos(2 * np.pi * carrier_freq * t)
    return message_signal, carrier_wave

def am_modulation(carrier, message, modulation_index):
    return carrier * (1 + modulation_index * message)

def fm_modulation(carrier_freq, message, t, modulation_index, amplitude_carrier):
    return amplitude_carrier * np.cos(2 * np.pi * carrier_freq * t + modulation_index * np.cumsum(message) / (t[1] - t[0]))

def pm_modulation(carrier_freq, message, t, modulation_index, amplitude_carrier):
    return amplitude_carrier * np.cos(2 * np.pi * carrier_freq * t + modulation_index * message)

SAMPLE_RATE = 1000
DURATION = 2
t = np.linspace(0, DURATION, int(SAMPLE_RATE * DURATION), endpoint=False)

CARRIER_FREQ = 100
MESSAGE_FREQ = 5
AMPLITUDE_CARRIER = 1
AMPLITUDE_MESSAGE = 1
MODULATION_INDEX = 0.8

message_signal, carrier_wave = create_signals(t, CARRIER_FREQ, MESSAGE_FREQ, AMPLITUDE_CARRIER, AMPLITUDE_MESSAGE, MODULATION_INDEX)
am_modulated = am_modulation(carrier_wave, message_signal, MODULATION_INDEX)
fm_modulated = fm_modulation(CARRIER_FREQ, message_signal, t, MODULATION_INDEX * CARRIER_FREQ, AMPLITUDE_CARRIER)
pm_modulated = pm_modulation(CARRIER_FREQ, message_signal, t, MODULATION_INDEX * np.pi, AMPLITUDE_CARRIER)

fig, axs = plt.subplots(4, 1, figsize=(10, 12))

axs[0].plot(t, message_signal)
axs[0].set_title('Message Signal')
axs[0].set_ylabel('Amplitude')

axs[1].plot(t, am_modulated)
axs[1].set_title('Amplitude Modulation (AM)')
axs[1].set_ylabel('Amplitude')

axs[2].plot(t, fm_modulated)
axs[2].set_title('Frequency Modulation (FM)')
axs[2].set_ylabel('Amplitude')

axs[3].plot(t, pm_modulated)
axs[3].set_title('Phase Modulation (PM)')
axs[3].set_ylabel('Amplitude')
axs[3].set_xlabel('Time (s)')

plt.tight_layout()
plt.show()

