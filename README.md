# PDDA_AoA

Calculate the spatial power spectrum based on "A New Low Complexity Angle of Arrival Algorithm for 1D and 2D Direction Estimation in MIMO Smart Antenna Systems" (Al-Sadoon et al 17)
DOI:10.3390/s17112631

```
sample_array = np.array([[-126+ 80j, -85+ -132j, 130+ -81j], [-78+ -128j, -127+ 82j, -72+ -141j]])

P_PDDA = calc_PDDA(sample_array)

theta = np.arange(-90, 90, 1)

plt.plot(theta, P_PDDA)
plt.xlabel("Angle [deg]")
plt.title(f"AoA: {theta[np.argmax(P_PDDA)]}")
```

![img_pdda](img_pdda.img)
