from random import random
from scipy import integrate
import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots()
x = np.linspace(0,3,100)
y = x**3
ax.plot(x,y)
l_x = []
l_y = []
for i in range(50):
   k = random()*3
   l_x.append(k);
   y1 = random()*27
   l_y.append(y1);
plt.scatter(l_x , l_y)
plt.show()

#інтегруємо функцію для знаходження площі
def f(x):
    return x**3
v, err = integrate.quad(f, 0, 3)
print("Площа фігури під функцією методом інтегрування "+str(round(v,2)))

#максимум функції та площа прямокутника, що охоплює функцію
max_y = 3**3
s_r = (3-0)*max_y
print("Площа прямокутника, що охоплює функцію "+str(s_r))

#шукаємо кількість точок під кривою
counter = 0
for i in range(50):
     x1 = l_x[i]
     y2 = x1**3
     if l_y[i] < y2:
         counter+=1
print("Загальна кількість точок 50")
print("Кількість точок під кривою "+ str(counter))

#обчислення інтегралу методом Монте-Карло.
s = s_r*(counter/50)
print("Площа під кривою "+ str(s))






