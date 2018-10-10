import numpy as np

def get_characteristics(signal, fs, min_frequency=None, max_frequency=None):
    fft = np.fft.fft(signal)
    freq = np.fft.fftfreq(len(signal), 1.0/fs)
    amplitudes = np.abs(fft)

    if (min_frequency is not None) and (max_frequency is not None):
        delta_f = float(fs) / len(signal)
        min_index = int(round(min_frequency / delta_f))
        max_index = int(round(max_frequency / delta_f))
        amplitudes = amplitudes[min_index:max_index + 1]
    else:
        min_index = 0

    dominant_index = np.argmax(amplitudes)
    index = min_index + dominant_index

    return [np.asscalar(amplitudes[dominant_index]), np.asscalar(np.abs(freq[index]))]
