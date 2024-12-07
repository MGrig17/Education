from matplotlib import pyplot
import numpy
from textwrap import wrap
import matplotlib.ticker as ticker
time2=[]
with open('time.txt') as f:
    for l in f:
        time2.append(float(l)**2)
h=[0, 0.005, 0.01, 0.015, 0.02, 0.025, 0.03, 0.035, 0.04, 0.045, 0.055, 0.065, 0.075]
h2=[i**2 for i in h]
k=4.06/10000
m_razr=1536.3
m_pf=983.2
r=0.05
I_platf=7.86
I_prak=[k*(m_pf+m_razr)*(i) for i in time2]
I_teor=[ (m_razr*(r**2)/2 +m_razr*(i)+ I_platf) for i in h2]
sign_h2=[0.001**2 for i in range(len(h))]
sign_y=[0.2 for i in range(len(h2))]

fig, ax=pyplot.subplots()


Y_std = [0.2 for i in range(len(h2))]
ax.errorbar(h2, I_prak, yerr=Y_std, fmt='o-g', capsize=4, elinewidth=1,linewidth=0.000001, ecolor='red', c='blue')

ax.scatter(h2, I_prak, c='blue', linewidth=0.2, label = 'практич')
ax.scatter(h2, I_teor, c='green', linewidth=0.2, label = 'теоретич')

z_prak=numpy.polyfit(h2, I_prak, 1)
p_prak=numpy.poly1d(z_prak)
y_prak=p_prak(h2)
ax.plot(h2, y_prak, c='blue')

z_teor=numpy.polyfit(h2, I_teor, 1)
p_teor=numpy.poly1d(z_teor)
y_teor=p_teor(h2)
ax.plot(h2, y_teor, c='green')

ax.legend(shadow = False, loc = 'right', fontsize = 10)
ax.set_ylabel("момент инерции, г*м^2")
ax.set_xlabel("расстояние^2, см^2")
ax.grid(which='major', color = 'k')
ax.minorticks_on()
ax.grid(which='minor', color = 'gray', linestyle = ':')
ax.xaxis.set_major_locator(ticker.MultipleLocator(0.001))
#  Устанавливаем интервал вспомогательных делений:
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.0002))

#  Тоже самое проделываем с делениями на оси "y":
ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.5))
# ax.axis([min(h2), max(h2)+0.0005, min(I_teor)-0.2, max(I_prak)+1])
# k=1667
# b=10.53
# appr=[k*i/1000 + b for i in range(100)]
# appr_x=[i/1000 for i in range(100)]
# ax.plot(appr_x, appr, 0.2,  c='purple')
print(p_teor)
print(p_prak)
pyplot.show()