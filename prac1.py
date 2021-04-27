import numpy as np
from math import sqrt, pi, exp
import matplotlib.pyplot as plt

N = 4096            # Number of samples
s = N/256           # standard deviation

y1 = []
for i in range(N):
  x = i - N/2
  v = np.sin(x)
  y1.append(v)

plt.figure(1)
plt.subplot(2, 1, 1)
plt.plot(y1)
plt.xlim([N/2-100, N/2+100])
plt.xlabel("Time")
plt.ylabel("Signal")

fk = np.fft.fft(y1)
plt.subplot(2, 1, 2)
plt.plot(np.abs(np.fft.fftshift(fk)))
plt.xlabel("Frequency")
plt.ylabel("Amplitude")
plt.show()

y2 = []
for i in range(N):
  x = i - N/2
  v = exp(-x**2/(2.0*s**2))/(sqrt(2*pi)*s)
  y2.append(v)

plt.figure(2)
plt.subplot(2, 1, 1)
plt.plot(y2)
plt.xlim([N/2-100, N/2+100])
plt.xlabel("Time")
plt.ylabel("Signal")

fk = np.fft.fft(y2)
plt.subplot(2, 1, 2)
plt.plot(np.abs(np.fft.fftshift(fk)))
plt.xlabel("Frequency")
plt.ylabel("Amplitude")
plt.show()

y1 = np.array(y1)
y2 = np.array(y2)
y3 = y1 * y2.T

plt.figure(3)
plt.subplot(2, 1, 1)
plt.plot(y3)
plt.xlim([N/2-100, N/2+100])
plt.xlabel("Time")
plt.ylabel("Signal")

fk = np.fft.fft(y3)
plt.subplot(2, 1, 2)
plt.plot(np.abs(np.fft.fftshift(fk)))
plt.xlabel("Frequency")
plt.ylabel("Amplitude")
plt.show()