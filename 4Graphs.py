import numpy as np
import matplotlib.pyplot as plt
import csv

x1 = []
y1 = []
x2 = []
y2 = []
x3 = []
y3 = []
x4 = []
y4 = []

with open('pyst.csv') as f:
    reader = csv.reader(f)
    flag = 0
    flag = 0
    index = 1
    index2 = 1
    index3 = 1
    index4 = 1
    for row in reader:
        if flag < 4:
            x1.append(float(row[0]))
            y1.append(index)
            index += 1
            flag += 1
        elif flag < 8:
            x2.append(float(row[0]))
            y2.append(index2)
            index2 += 1
            flag += 1
        elif flag < 12:
            x3.append(float(row[0]))
            y3.append(index3)
            index3 += 1
            flag += 1
        else:
            x4.append(float(row[0]))
            y4.append(index4)
            index4 += 1
            flag += 1

print(x1)
print(y1)
print(x2)
print(y2)
print(x3)
print(y3)
print(x4)
print(y4)

fig1, ax1 = plt.subplots(2,2)

p1 = np.polyfit(y1,x1, 1)
p2 = np.polyfit(y2,x2, 1)
p3 = np.polyfit(y3,x3, 1)
p4 = np.polyfit(y4,x4, 1)

ya1 = np.polyval(p1, y1)
ya2 = np.polyval(p2, y1)
ya3 = np.polyval(p3, y1)
ya4 = np.polyval(p4, y1)

ax1[0,0].plot(y1, ya1,color = "black", marker = '.', label = "2726 Гц")
ax1[1,0].plot(y2, ya2,color = "black", marker = '.', label = "3352 Гц")
ax1[0,1].plot(y3, ya3,color = "black", marker = '.', label = "3528 Гц")
ax1[1,1].plot(y4, ya4,color = "black", marker = '.', label = "3040 Гц")

ax1[0,0].set_title("k1 = 6.45")
ax1[1,0].set_title("k2 = 5.19")
ax1[0,1].set_title("k3 = 4.97")
ax1[1,1].set_title("k4 = 5.76")

ax1[0,0].set_yticks(np.arange(0,24,2))
ax1[0,0].set_xticks(np.arange(0,4.5,0.5))
ax1[1,0].set_yticks(np.arange(0,24,2))
ax1[1,0].set_xticks(np.arange(0,4.5,0.5))
ax1[0,1].set_yticks(np.arange(0,24,2))
ax1[0,1].set_xticks(np.arange(0,4.5,0.5))
ax1[1,1].set_yticks(np.arange(0,24,2))
ax1[1,1].set_xticks(np.arange(0,4.5,0.5))

ax1[0,0].grid(color='black', linewidth=0.15)
ax1[1,0].grid(color='black', linewidth=0.15)
ax1[0,1].grid(color='black', linewidth=0.15)
ax1[1,1].grid(color='black', linewidth=0.15)

ax1[0,0].set_ylabel('ΔL, см')
ax1[0,1].set_ylabel('ΔL, см')
ax1[1,1].set_ylabel('ΔL, см')
ax1[1,0].set_ylabel('ΔL, см')

ax1[0,0].legend(loc='lower right')
ax1[1,0].legend(loc='lower right')
ax1[0,1].legend(loc='lower right')
ax1[1,1].legend(loc='lower right')

for i in range(4):
    ax1[0, 0].plot(y1[i], x1[i], color='red', marker='*')
    ax1[1, 0].plot(y2[i], x2[i], color='red', marker='*')
    ax1[0, 1].plot(y3[i], x3[i], color='red', marker='*')
    ax1[1, 1].plot(y4[i], x4[i], color='red', marker='*')

plt.show()