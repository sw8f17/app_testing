from scipy.io import wavfile
import numpy as np
from numpy.fft import fft, ifft, fftshift
import begin
from itertools import combinations
from glob import glob
import os.path
from matplotlib import pyplot as plt


def _cross_correlation_using_fft(x, y):
    """
    Make cross correlation between two signals using fft

    :param x: Sample 1
    :param y: sample 2
    :returns: Cross correlation of sample 1 and 2
    """
    f1 = fft(x)
    f2 = fft(np.flipud(y))
    cc = np.real(ifft(f1 * f2))
    return fftshift(cc)


def _compute_shift(x, y):
    """
    Compute the time shift of signal y in regards to signal x

    :param x: Sample 1
    :param y: sample 2
    :returns: < 0 means that y starts 'shift' time steps before x
        > 0 means that y starts 'shift' time steps after x
    """
    assert len(x) == len(y)
    c = _cross_correlation_using_fft(x, y)
    assert len(c) == len(x)
    zero_index = int(len(x) / 2) - 1
    shift = zero_index - np.argmax(np.abs(c))
    return shift


@begin.start(auto_convert=True)
def main(in_file: 'Wavfile(s) to test. Glob syntax can be used'):
    for file in glob(in_file):
        print("\nFile:", os.path.basename(file), end='')
        rate = 0
        audio = None
        try:
            rate, audio = wavfile.read(file)
        except:
            print("  Not wav file!")
            continue
        print("  [{} channels, {:.2f} sec. {} Hz]".format(audio.shape[1], audio.shape[0] / rate, rate))
        for pair in combinations(range(audio.shape[1]), 2):
            print("  Ch. {} -> {}:".format(*pair), end='')
            shift = _compute_shift(audio[:, pair[1]], audio[:, pair[0]])
            print(" {:>5} sample(s) [{:>7,.3f} ms]".format(shift, shift / (rate / 1000)))