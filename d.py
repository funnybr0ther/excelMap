from numpy import *
import matplotlib.pyplot as plt

filename = "pH.tsv"
with(open(filename, "r")) as file:
    lines = file.read().splitlines()
    lines = lines[1:]


def readColumns(d):
    if d == 7:
        t = empty(0)
        v = empty(0)
        for i in range(0, len(lines)-2):
            line = lines[i]
            t = append(t, [float(line.split("\t")[1])])
        amp = float(lines[-2].split("\t")[1])
        v = float(lines[-1].split("\t")[1])
        return t, v, amp
    if d==11:
        t = empty(0)
        v = empty(0)
        for i in range(0, len(lines)-2):
            line = lines[i]
            t = append(t, [float(line.split("\t")[2])])
        amp = float(lines[-2].split("\t")[2])
        v = float(lines[-1].split("\t")[2])
        return t, v,amp
    if d==15:
        t = empty(0)
        v = empty(0)
        for i in range(0, len(lines)-2):
            line = lines[i]
            t = append(t, [float(line.split("\t")[3])])
        amp = float(lines[-2].split("\t")[3])
        v = float(lines[-1].split("\t")[3])
        return t, v,amp
    if d==19:
        t = empty(0)
        v = empty(0)
        for i in range(0, len(lines)-2):
            line = lines[i]
            t = append(t, [float(line.split("\t")[4])])
        amp = float(lines[-2].split("\t")[4])
        v = float(lines[-1].split("\t")[4])
        return t, v,amp

liters = empty(0)
for i in range(0,len(lines)-2):
    liters = append(liters,[float(lines[i].split("\t")[0])])

temps7,volts7,i7 = readColumns(7)
temps11,volts11,i11 = readColumns(11)
temps15, volts15, i15 = readColumns(15)
temps19, volts19, i19 = readColumns(19)

time_x = linspace(0, max([temps7[-1], temps11[-1], temps15[-1], temps19[-1]]), 1000)
fit7 = polyfit(temps7, liters, 1)
fit11 = polyfit(temps11, liters, 1)
fit15 = polyfit(temps15, liters, 1)
fit19 = polyfit(temps19, liters, 1)

plt.plot(time_x, polyval(fit7, time_x), "r", label="d=7")
plt.plot(time_x, polyval(fit11, time_x), "g", label="d=11")
plt.plot(time_x, polyval(fit15, time_x), "b", label="d=15")
plt.plot(time_x, polyval(fit19, time_x), "m", label="d=19")
plt.xlabel("t")
plt.ylabel("H2 (m^3)")
plt.legend()
plt.savefig("d_1.pdf",format="pdf")
plt.show()

speed7 = fit7[0]
speed11=fit11[0]
speed15=fit15[0]
speed19 = fit19[0]

interpol2 = polyfit(array([7,11,15,19]), array([speed7, speed11, speed15, speed19]), 1)
pHx = linspace(7,19,1000)
plt.plot(array([7,11,15,19]), array([speed7, speed11, speed15, speed19]), ".r")
plt.plot(pHx,polyval(interpol2,pHx),"b")
plt.xlabel("d")
plt.ylabel("vitesse")
plt.savefig("d_2.pdf",format="pdf")
plt.show()

v7 = i7 * temps7[-1] * 8.314 * 298 / (2 * 96500 * 100000)
v11 = i11 * temps11[-1] * 8.314 * 298 / (2 * 96500 * 100000)
v15 = i15 * temps15[-1] * 8.314 * 298 / (2 * 96500 * 100000)
v19 = i19 * temps19[-1] * 8.314 * 298 / (2 * 96500 * 100000)

f7 = v7 / (10 ** -4)
f11 = v11 / (10 ** -4)
f15 = v15 / (10 ** -4)
f19 = v19 / (10 ** -4)



e7 = (((10 ** -4) * 100000 / (8.314 * 298)) * (285 * 1000)) / (volts7 * i7 * temps7[-1])
e11 = (((10 ** -4) * 100000 / (8.314 * 298)) * (285 * 1000)) / (volts11 * i11 * temps11[-1])
e15 = (((10 ** -4) * 100000 / (8.314 * 298)) * (285 * 1000)) / (volts15 * i15 * temps15[-1])
e19 = (((10 ** -4) * 100000 / (8.314 * 298)) * (285 * 1000)) / (volts19 * i19 * temps19[-1])

interpol3 = polyfit(array([7,11,15,19]), array([f7, f11, f15, f19]), 1)
pHx = linspace(7,19,1000)
plt.plot(array([7,11,15,19]), array([f7, f11, f15, f19]), ".r")
plt.plot(pHx,polyval(interpol3,pHx),"b")
plt.xlabel("I")
plt.ylabel("Rendement Faradique")
plt.savefig("I_3.pdf",format="pdf")
plt.show()

interpol4 = polyfit(array([7,11,15,19]), array([e7, e11, e15, e19]), 1)
pHx = linspace(7,19,1000)
plt.plot(array([7,11,15,19]), array([e7, e11, e15, e19]), ".r")
plt.plot(pHx,polyval(interpol4,pHx),"b")
plt.xlabel("I")
plt.ylabel("Rendement Energetique")
plt.savefig("I_4.pdf",format="pdf")
plt.show()



