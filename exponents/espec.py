import numpy as np
from matplotlib import pyplot as plt

x = np.arange(-1.0,5.0,0.1)
ey = [(np.e ** n) for n in x]
derivative_e = [(n * np.e) for n in x]

#e is a special number because it's derivative
#is the same as the number itself
epointx = [1]
epointy = [np.e]

plt.plot(x,ey,label='e^x')
plt.plot(x,derivative_e,color='orangered',label='derivative e^x')
plt.scatter(epointx,epointy,color='red')

#any other number raised to x
#dy = [(2 ** f) for f in x]
#derivative_dy = [(g * 2) for g in x]
#plt.plot(x,dy,color='green',label="3.25^x")
#plt.plot(x,derivative_dy,color='purple',label='derivative 3.25^x')

plt.title("e and it's derivative")
plt.legend()
plt.show()