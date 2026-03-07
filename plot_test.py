import numpy as np
import matplotlib.pyplot as plt
import qutip as qt

t = np.linspace(0, 10, 200)
plt.plot(t, np.cos(t))
plt.title("Matplotlib ok")
plt.show()