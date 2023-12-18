import numpy
import matplotlib.pyplot as plt


x = numpy.linspace(0,5,100)

y1 = numpy.exp(x)


plt.plot(x,y1, color = 'red')

plt.xlabel('czas t')
plt.ylabel('predkosc v')
plt.ylim((0,300))

plt.legend(['ferrari'])

plt.show()






