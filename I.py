from numpy import *
import matplotlib.pyplot as plt

filename = "pH.tsv"
with(open(filename, "r")) as file:
    lines = file.read().splitlines()
    lines = lines[1:]


def readColumns(I):
    if I == 0.25:
        t = empty(0)
        v = empty(0)
        for i in range(0, len(lines)-2):
            line = lines[i]
            t = append(t, [float(line.split("\t")[1])])
        amp = float(lines[-2].split("\t")[1])
        v = float(lines[-1].split("\t")[1])
        return t, v, amp
    if I == 0.50:
        t = empty(0)
        v = empty(0)
        for i in range(0, len(lines)-2):
            line = lines[i]
            t = append(t, [float(line.split("\t")[2])])
        amp = float(lines[-2].split("\t")[2])
        v = float(lines[-1].split("\t")[2])
        return t, v,amp
    if I == 0.75:
        t = empty(0)
        v = empty(0)
        for i in range(0, len(lines)-2):
            line = lines[i]
            t = append(t, [float(line.split("\t")[3])])
        amp = float(lines[-2].split("\t")[3])
        v = float(lines[-1].split("\t")[3])
        return t, v,amp
    if I == 1:
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

temps25,volts25,i25 = readColumns(0.25)
temps50,volts50,i50 = readColumns(0.50)
temps75,volts75,i75 = readColumns(0.75)
temps100,volts100,i100 = readColumns(1)

time_x = linspace(0,max([temps25[-1],temps50[-1],temps75[-1],temps100[-1]]),1000)
fit25 = polyfit(temps25,liters,1)
fit50 = polyfit(temps50,liters,1)
fit75 = polyfit(temps75,liters,1)
fit100 = polyfit(temps100,liters,1)

plt.plot(time_x,polyval(fit25,time_x),"r",label="I = 0.25")
plt.plot(time_x,polyval(fit50,time_x),"g",label="I = 0.50")
plt.plot(time_x,polyval(fit75,time_x),"b",label="I = 0.75")
plt.plot(time_x,polyval(fit100,time_x),"m",label="I = 1")
plt.xlabel("t")
plt.ylabel("H2 (m^3)")
plt.legend()
plt.savefig("I_1.pdf",format="pdf")
plt.show()

speed25 = fit25[0]
speed50=fit50[0]
speed75=fit75[0]
speed100 = fit100[0]

interpol2 = polyfit(array([0.25,0.5,0.75,1]),array([speed25,speed50,speed75,speed100]),1)
pHx = linspace(0,1,1000)
plt.plot(array([0.25,0.50,0.75,1]),array([speed25,speed50,speed75,speed100]),".r")
plt.plot(pHx,polyval(interpol2,pHx),"b")
plt.xlabel("I")
plt.ylabel("vitesse")
plt.savefig("d_2.pdf",format="pdf")
plt.show()

v25 = i25*temps25[-1]*8.314*298/(2*96500*100000)
v50 = i50*temps50[-1]*8.314*298/(2*96500*100000)
v75 = i75*temps75[-1]*8.314*298/(2*96500*100000)
v100 = i100*temps100[-1]*8.314*298/(2*96500*100000)

f25 = v25/(10**-4)
f50 = v50/(10**-4)
f75 = v75/(10**-4)
f100 = v100/(10**-4)



e25 = (((10**-4)*100000/(8.314*298))*(285*1000))/(volts25*i25*temps25[-1])
e50 = (((10**-4)*100000/(8.314*298))*(285*1000))/(volts50*i50*temps50[-1])
e75 = (((10**-4)*100000/(8.314*298))*(285*1000))/(volts75*i75*temps75[-1])
e100 = (((10**-4)*100000/(8.314*298))*(285*1000))/(volts100*i100*temps100[-1])

interpol3 = polyfit(array([0.25,0.50,0.75,1]),array([f25,f50,f75,f100]),1)
pHx = linspace(0,1,1000)
plt.plot(array([0.25,0.50,0.75,1]),array([f25,f50,f75,f100]),".r")
plt.plot(pHx,polyval(interpol3,pHx),"b")
plt.xlabel("I")
plt.ylabel("Rendement Faradique")
plt.savefig("I_3.pdf",format="pdf")
plt.show()

interpol4 = polyfit(array([0.25,0.50,0.75,1]),array([e25,e50,e75,e100]),1)
pHx = linspace(0,1,1000)
plt.plot(array([0.25,0.50,0.75,1]),array([e25,e50,e75,e100]),".r")
plt.plot(pHx,polyval(interpol4,pHx),"b")
plt.xlabel("I")
plt.ylabel("Rendement Energetique")
plt.savefig("I_4.pdf",format="pdf")
plt.show()



