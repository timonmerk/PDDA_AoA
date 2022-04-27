import numpy as np
from matplotlib import pyplot as plt

def calc_PDDA(data_IQ : np.array) -> np.array:
    """
    Calculate the spatial power spectrum based on "A New Low Complexity
    Angle of Arrival Algorithm for 1D and 2D Direction Estimation
    in MIMO Smart Antenna Systems" (Al-Sadoon et al 17)
    DOI:10.3390/s17112631


    data_IQ : np array, shape (sampling_sequences, antenna_elements)
    """

    c = 299792458  # light speed
    freq = 2.48 * 10**9  #  transmission frequency Hz
    lambda_ = c / freq
    beta = 2*np.pi / lambda_
    spacing = 0.05  # antenna element spacing m

    const_SV = beta * spacing

    X_t = sample_array.T
    h = np.expand_dims(X_t[0,:], axis=0)
    H = X_t[1:,:]

    p = np.matmul(h, H.T) / np.matmul(h,h.T);

    e = np.zeros(3, dtype=complex)
    e[0] = 1 + 0.j
    e[1:] = p

    theta = np.arange(-90, 90, 1)

    P_PDDA = np.zeros([theta.shape[0]])
    num_ant = 3
    for i in range(theta.shape[0]):

        steer_vect = np.exp(-1j*const_SV * np.sin(np.deg2rad(theta[i])) * np.array([0,1,2]))

        P_PDDA[i] = np.abs(np.matmul(steer_vect, e))**2

    return P_PDDA

def main():
    # 3 Antenna Elements, sampled 2 times
    sample_array = np.array([[-126+ 80j, -85+ -132j, 130+ -81j], [-78+ -128j, -127+ 82j, -72+ -141j]])

    P_PDDA = calc_PDDA(sample_array)
    theta = np.arange(-90, 90, 1)
    plt.plot(theta, P_PDDA)
    plt.xlabel("Angle [deg]")
    plt.title(f"AoA: {theta[np.argmax(P_PDDA)]}")

if __name__ == "__main__":
    main()
