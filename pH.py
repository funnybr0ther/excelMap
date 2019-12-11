from numpy import *
import matplotlib.pyplot as plt

filename = "pH.tsv"
with(open("pH.tsv", "r")) as file:
    lines = file.read().splitlines()
    lines = lines[1:]


def readColumns(pH):
    if pH == 13:
        t = empty(0)
        v = empty(0)
        for i in range(0, len(lines)-2):
            line = lines[i]
            t = append(t, [float(line.split("\t")[1])])
        amp = float(lines[-2].split("\t")[1])
        v = float(lines[-1].split("\t")[1])
        return t, v,amp
    if pH == 13.5:
        t = empty(0)
        v = empty(0)
        for i in range(0, len(lines)-2):
            line = lines[i]
            t = append(t, [float(line.split("\t")[2])])
        amp = float(lines[-2].split("\t")[2])
        v = float(lines[-1].split("\t")[2])
        return t, v,amp
    if pH == 14:
        t = empty(0)
        v = empty(0)
        for i in range(0, len(lines)-2):
            line = lines[i]
            t = append(t, [float(line.split("\t")[3])])
        amp = float(lines[-2].split("\t")[3])
        v = float(lines[-1].split("\t")[3])
        return t, v,amp

liters = empty(0)
for i in range(0,len(lines)-2):
    liters = append(liters,[float(lines[i].split("\t")[0])])

temps13,volts13,i13 = readColumns(13)
temps135,volts135,i135 = readColumns(13.5)
temps14,volts14,i14 = readColumns(14)

time_x = linspace(0,max([temps13[-1],temps14[-1],temps135[-1]]),1000)
fit13 = polyfit(temps13,liters,1)
fit135 = polyfit(temps135,liters,1)
fit14 = polyfit(temps14,liters,1)

plt.plot(time_x,polyval(fit13,time_x),"r",label="pH = 13")
plt.plot(time_x,polyval(fit135,time_x),"g",label="pH = 13.5")
plt.plot(time_x,polyval(fit14,time_x),"b",label="pH = 14")
plt.xlabel("t")
plt.ylabel("H2 (m^3)")
plt.legend()
plt.savefig("ph_1.pdf",format="pdf")
plt.show()

speed13 = fit13[0]
speed135=fit135[0]
speed14=fit14[0]

interpol2 = polyfit(array([13,13.5,14]),array([speed13,speed135,speed14]),1)
pHx = linspace(13,14,1000)
plt.plot(array([13,13.5,14]),array([speed13,speed135,speed14]),".r")
plt.plot(pHx,polyval(interpol2,pHx),"b")
plt.xlabel("pH")
plt.ylabel("vitesse")
plt.savefig("ph_2.pdf",format="pdf")
plt.show()

v13 = i13*temps13[-1]*8.314*298/(2*96500*100000)
v135 = i135*temps135[-1]*8.314*298/(2*96500*100000)
v14 = i14*temps14[-1]*8.314*298/(2*96500*100000)

f13 = v13/(10**-4)
f135 = v135/(10**-4)
f14 = v14/(10**-4)

e13 = (((10**-4)*100000/(8.314*298))*(285*1000))/(volts13*i13*temps13[-1])
e135 = (((10**-4)*100000/(8.314*298))*(285*1000))/(volts135*i135*temps135[-1])
e14 = (((10**-4)*100000/(8.314*298))*(285*1000))/(volts14*i14*temps14[-1])

interpol3 = polyfit(array([13,13.5,14]),array([f13,f135,f14]),1)
pHx = linspace(13,14,1000)
plt.plot(array([13,13.5,14]),array([f13,f135,f14]),".r")
plt.plot(pHx,polyval(interpol3,pHx),"b")
plt.xlabel("pH")
plt.ylabel("Rendement Faradique")
plt.savefig("ph_3.pdf",format="pdf")
plt.show()


interpol4 = polyfit(array([13,13.5,14]),array([e13,e135,e14]),1)
pHx = linspace(13,14,1000)
plt.plot(array([13,13.5,14]),array([e13,e135,e14]),".r")
plt.plot(pHx,polyval(interpol4,pHx),"b")
plt.xlabel("pH")
plt.ylabel("Rendement Energétique")
plt.savefig("ph_4.pdf",format="pdf")
plt.show()




