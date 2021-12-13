import numpy as np
from numpy.core.numeric import zeros_like
from scipy import signal
import matplotlib.pyplot as plt
from scipy import interpolate

end_energy = 100.0
samples = 5000
energies = np.linspace(0, end_energy, samples)

reference_sigma = 1.0

squares = np.zeros_like(energies)
# plt.plot(energies, squares)
dE_width = np.abs(7*np.sin(0.5*np.pi*energies / end_energy)**4.0)+1

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





# incremental_energies = (end_energy/samples)*np.ones_like(energies) # first assume linear sampling
# warped_incremental_energies = incremental_energies / (dE_width/np.min(dE_width))
# warped_energies = np.cumsum(warped_incremental_energies) - warped_incremental_energies[0]

# warped_new_uniform_grid = np.linspace(0,warped_energies[-1], samples)
# re_sampled_warped_convolved = interpolate.interp1d(warped_energies, convolved)(warped_new_uniform_grid)





def warp_array(input_function, energies, warp_function):
    incremental_energies = (energies[-1]/len(energies))*np.ones_like(energies) # first assume linear sampling
    warped_incremental_energies = incremental_energies / (warp_function/np.min(warp_function))
    warped_energies = np.cumsum(warped_incremental_energies) - warped_incremental_energies[0]

    warped_new_uniform_grid = np.linspace(0,warped_energies[-1], samples)
    re_sampled_warped_convolved = interpolate.interp1d(warped_energies, input_function)(warped_new_uniform_grid)

    return warped_new_uniform_grid, re_sampled_warped_convolved

warped_new_uniform_grid, re_sampled_warped_convolved = warp_array(convolved, energies, dE_width)

unwarped_energies, unwarped = warp_array(re_sampled_warped_convolved, warped_new_uniform_grid, np.flip(dE_width))


# def unwarp_array(warped_array, energy_width_function, reference_sigma, warped_new_uniform_grid, original_energy_spacing):
#     incremental_energies = (original_energy_spacing[-1]/samples)*np.ones_like(original_energy_spacing) # first assume linear sampling

#     # unwarped_incremental_energies = incremental_energies * (np.abs(energy_width_function - reference_sigma))

#     # global warped_incremental_energies
#     unwarped_incremental_energies = warped_incremental_energies * (np.abs(dE_width - reference_sigma) + 1)

#     global warped_energies
#     energies-warped_energies
#     # unwarped_energies = np.cumsum(unwarped_incremental_energies) - unwarped_incremental_energies[0]

#     # re-sample to uniform spacing
#     # unwarped_convolved = interpolate.interp1d(unwarped_energies, warped_array, fill_value="extrapolate")(original_energy_spacing)
#     # return unwarped_convolved
#     return unwarped_energies, warped_array

# a,b = unwarp_array(re_sampled_warped_convolved, dE_width, reference_sigma, warped_new_uniform_grid, energies)

# # nonstationary

plt.subplot(4,1,1)
plt.plot(energies, dE_width)
plt.subplot(4,1,2)
# plt.plot(energies, squares)
plt.plot(energies,convolved)

plt.subplot(4,1,3)
# plt.plot(warped_energies,convolved)
plt.plot(warped_new_uniform_grid,re_sampled_warped_convolved)

plt.subplot(4,1,4)

plt.plot(unwarped_energies,unwarped)

plt.show()




