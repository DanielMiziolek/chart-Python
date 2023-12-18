import numpy
import matplotlib.pyplot as plt


x = numpy.linspace(0,5,1)
y1 = numpy.sin(x)
y2 = numpy.exp(x)

plt.plot(x,y1)
plt.plot(x,y2)

plt.legend(['Hamilton(x)','Verstappen(x)'])
plt.show()
