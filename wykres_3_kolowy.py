import matplotlib.pyplot as plt




nazwa = ['mercedes', 'porshe', 'audi', 'bmw', 'lamborghini', 'wolswagen', 'ferrari']
procent = [29.9, 19.1, 8.2, 7.3, 6.2, 5.9, 76.6]
colors = ['white', 'green', 'gray', 'blue', 'purple', 'yellow', 'red']


plt.pie(procent,
        labels=nazwa,
        colors=colors,
        explode=(0, 0, 0, 0, 0, 0,0),
        autopct='%.1f%%'
        )

plt.title("najlepsze auta według Daniela")



plt.show()

