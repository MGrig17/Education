from matplotlib import pyplot as plt

def MNK(x,y,n):
    a1, a2, a3, mx, my = 0, 0, 0, 0, 0
    for i in range(n):
        a1 += (x[i] * y[i])
        a2 += ((x[i]) ** 2)
        a3 += ((y[i]) ** 2)
        mx += ((x[i]))
        my += (y[i])
        if (i == n-1):
            a1 /= n
            a2 /= n
            a3 /= n
            mx /= n
            my /= n
    k = (a1 - mx * my) / (a2 - (mx ** 2))
    b = my - k * mx
    sig_k = 1/((n)**0.5) * (((a3 - (my ** 2)) / (a2 - (mx ** 2))) - k**2) ** 0.5
    print(k, ' ',sig_k," ", b)
    return (k,sig_k,b)

import matplotlib.pyplot as plt
name40='wave-data-40mm-kalibr.txt'
name60='wave-data-60mm-kalibr.txt'
name80='wave-data-80mm-kalibr.txt'
name100='wave-data-100mm-kalibr.txt'
name120='wave-data-120mm-kalibr.txt'

Sred40=0
Sred60=0
Sred80=0
Sred100=0
Sred120=0

V40,V60,V80,V100,V120=0,0,0,0,0


with open(name40,'r') as file:
    V40 = float(file.readline())
    for l in range (100):
        Sred40 += float(file.readline())
    Sred40 /= 100

with open(name60,'r') as file:
    V60 = float(file.readline())
    for l in range (100):
        Sred60 += float(file.readline())
    Sred60 /= 100

with open(name80,'r') as file:
    V80 = float(file.readline())
    for l in range (100):
        Sred80 += float(file.readline())
    Sred80 /= 100

with open(name100,'r') as file:
    V100 = float(file.readline())
    for l in range (100):
        Sred100 += float(file.readline())
    Sred100 /= 100

with open(name120,'r') as file:
    V120 = float(file.readline())
    for l in range (100):
        Sred120 += float(file.readline())
    Sred120 /= 100



plt.scatter(Sred40,40,c='red')
plt.scatter(Sred60,60,c='blue')
plt.scatter(Sred80,80,c='green')
plt.scatter(Sred100,100,c='black')
plt.scatter(Sred120,120,c='ORANGE')

sred=[Sred40,Sred60,Sred80,Sred100,Sred120]
mm=[40,60,80,100,120]
print(sred)
k,sig_k,b=MNK(sred,mm,5)

print("Коэф перевода наряжения в мм k_0 = ",float(int((1/k)*100))/100)
plt.plot([0.6, 1.6], [0.6*k+b, 1.6*k+b],c='purple',label="k = %.4f b=%.4f" %(k, b))
plt.xlabel("мм")
plt.ylabel("В")
plt.legend()
plt.show()

