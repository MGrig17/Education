from matplotlib import pyplot as plt

def MNK(x,y,p,n,kof):
    a1, a2, a3, mx, my = 0, 0, 0, 0, 0
    for i in range(p,n):
        a1 += (x[i] * (kof*(y[i])))
        a2 += ((x[i]) ** 2)
        a3 += ((kof*(y[i])) ** 2)
        mx += ((x[i]))
        my += ((kof*(y[i])))
        if (i == n-p-1):
            a1 /= (n-p)
            a2 /= (n-p)
            a3 /= (n-p)
            mx /= (n-p)
            my /= (n-p)
    k = (a1 - mx * my) / (a2 - (mx ** 2))
    b = my - k * mx
    sig_k = 1/(((n-p))**0.5) * (((a3 - (my ** 2)) / (a2 - (mx ** 2))) - k**2) ** 0.5
    print(k, ' ',sig_k," ", b)
    return (k,sig_k,b)


import matplotlib.pyplot as plt
name40='wave-data-40mm.txt'
name60='wave-data-60mm-1.txt'
name80='wave-data-80mm.txt'
name100='wave-data-100mm.txt'
name120='wave-data-120mm.txt'





k=92.16
v_40=300*[0]
time_40=300*[0]
plt.figure(1)
with open(name40, 'r') as file:
    n = 253
    t40 = float(file.readline())
    t2=float(file.readline())
    for i in range(n):
        t1=t2
        v_40[i]=t1
        time_40[i]=t40 / n * i
        plt.scatter(t40 / n * i, k*t1, c="red",s = 5)
        t2=float(file.readline())
        plt.plot([t40 / n * i,t40 / n * (i+1)], [t1 * k,t2 * k], c='red')
    ker = 52
    num = 80
    k1, sig_k1, b1 = MNK(time_40, v_40, 0, ker,1)
    k2, sig_k2, b2 = MNK(time_40,v_40,ker,num,-1)
    plt.plot([time_40[0], (time_40[ker]+0.5)], [(time_40[0] * k1 + b1) * k, (time_40[ker] * k1 + b1) * k], c='blue')
    plt.plot([time_40[ker], time_40[num]], [(time_40[ker] * (k2) + b2) * k , (time_40[num] * (k2) + b2) * k], c='green')
    #plt.plot([time_40[0], (time_40[ker+50]+0.5)], [(time_40[0] * k1 + b1) * k, (time_40[ker+50] * k1 + b1) * k], c='black')
    print(k2)





    # plt.scatter(t40 / n * 52, 65, c="blue", s=5)
    #
    # for i in range(52,n):
    #     list1 = (i-51) * [0]
    #     list1[i-52-1] = t_40[i]
    #     k,sig_k,b=MNK(time_40,t_40,i-52)



plt.xlabel("t, сек")
plt.ylabel("l, см")
plt.title("40")










# plt.figure(2)
# with open(name60, 'r') as file:
#     n = 196
#     t60 = float(file.readline())
#     t2=float(file.readline())
#     for i in range(n):
#         t1=t2
#         plt.scatter(t60 / n * i, k*t1, c="red",s = 5)
#         t2=float(file.readline())
#         plt.plot([t60 / n * i,t60 / n * (i+1)], [t1 * k,t2 * k], c='red')
#
# plt.xlabel("t, сек")
# plt.ylabel("l, см")
# plt.title("60")
#
# plt.figure(3)
# with open(name80, 'r') as file:
#     n = 120
#     t80 = float(file.readline())
#     t2=float(file.readline())
#     for i in range(n):
#         t1=t2
#         plt.scatter(t80 / n * i, k*t1, c="red",s = 5)
#         t2=float(file.readline())
#         plt.plot([t80 / n * i,t80 / n * (i+1)], [t1 * k,t2 * k], c='red')
#
# plt.xlabel("t, сек")
# plt.ylabel("l, см")
# plt.title("80")
#
#
# plt.figure(4)
# with open(name100, 'r') as file:
#     n = 108
#     t100 = float(file.readline())
#     t2=float(file.readline())
#     for i in range(n):
#         t1=t2
#         plt.scatter(t100 / n * i, k*t1, c="red",s = 5)
#         t2=float(file.readline())
#         plt.plot([t100 / n * i,t100 / n * (i+1)], [t1 * k,t2 * k], c='red')
#
# plt.xlabel("t, сек")
# plt.ylabel("l, см")
# plt.title("100")
#
# plt.figure(5)
# with open(name120, 'r') as file:
#     n = 108
#     t120 = float(file.readline())
#     t2=float(file.readline())
#     for i in range(n):
#         t1=t2
#         plt.scatter(t120 / n * i, k*t1, c="red",s = 5)
#         t2=float(file.readline())
#         plt.plot([t120 / n * i,t120 / n * (i+1)], [t1 * k,t2 * k], c='red')
#
# plt.xlabel("t, сек")
# plt.ylabel("l, см")
# plt.title("120")







#
# plt.figure(2)
# v_60=n*[0]
# t_60=n*[0]
# with open(name60, 'r') as file:
#     t60 = float(file.readline())
#     for i in range(n):
#         v=float(file.readline())
#         v_60[i]=v
#         t_60[i]=t60 / n * i
#         plt.scatter(t60 / n * i, k*v, c="red",s = 5)
#
# print(t_60)
# print(v_60)
# plt.plot(t_60,v_60,c='red')
#
# plt.xlabel("t, сек")
# plt.ylabel("l, см")


plt.show()