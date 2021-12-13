import numpy as np
from numpy.core.numeric import zeros_like
from scipy import signal
import matplotlib.pyplot as plt


end_energy = 100.0
samples = 3000
energies = np.linspace(0, end_energy, samples)

squares = np.zeros_like(energies)
# plt.plot(energies, squares)
dE_width = np.abs(5*np.sin(0.5*np.pi*energies / end_energy)**4.0)+1

def gaussian(x, mu, sig):
    return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))


squares[0:samples//4] = 1.0

squares[samples-(samples//4):] = 1.0

convolved = np.copy(squares)
# steps = 20
# for i in np.arange(0, 1000, steps):
kernel = gaussian(energies,0,dE_width[samples//4])
kernel /= np.sum(kernel)

# dealing with convolution windows is pretty confusing. Wonder if there's a better way.
convolved[samples//4:+samples//2] = np.convolve(squares, kernel,mode='same')[samples//2:samples//2+samples//4]

kernel = gaussian(energies,0,dE_width[samples//2 + samples//4])
kernel /= np.sum(kernel)
convolved[samples//2:samples//2+samples//4] = np.flip(np.convolve(squares, kernel,mode='same')[samples//2:samples//2+samples//4])


# # nonstationary
#     # 
#     convolved_squares[i:i+(1000//steps)] = convolved[i:i+(1000//steps)]


plt.plot(energies, dE_width)
plt.plot(energies, squares)
plt.plot(energies,convolved)

plt.show()
