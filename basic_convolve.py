






for i in range(max_iterations):
    # convolution is commutative
    P_conv_On = np.convolve(ret,point_spread_function, mode='same') + 1e-12
    # plt.plot(np.arange(len(P_conv_On)), P_conv_On)
    # plt.plot(np.arange(len(yext)), yext)
    # plt.show()
    I_over_P_conv_On = yext/P_conv_On # zeros nan here 
    error_estimate = np.convolve(I_over_P_conv_On,flipped_point_spread_function, mode='same')


    # re-smooth each iteration - the "regularizing filter"
    # ret = ret * error_estimate
    ret = gaussian_filter(ret * error_estimate, regularization_filter_width)

    chi_squared = np.sum(((P_conv_On - yext)**2) / yext)
    chi_squared *= 1.0 / len(yext) 
    convergence.append(chi_squared)

convergence = np.array(convergence)