from numpy import *
import matplotlib.pyplot as plt
from matplotlib import rc


def plotmaker(filename):
    x = empty(0)
    y = empty(0)
    with open(filename, "r") as file:
        lines = file.read().splitlines()
    for line in lines:
        x = append(x, [float(line.split("&")[0])])
        y = append(y, [float(line.split("&")[1])])
    return x, y


x, y = plotmaker("file.tsv")
mini = min(x)
maxi = max(x)
x_label = input("Label en X")
y_label = input("Label en Y")
filename = input("Nom du pdf?")
title = input("Titre?")
interpol = polyval(polyfit(x, y, 1), linspace(mini, maxi, 1000))
plt.plot(x, y, ".r")
plt.plot(linspace(mini, maxi, 1000), interpol)
plt.xlabel(x_label)
plt.ylabel(y_label)
plt.title(title)
plt.savefig(filename + ".pdf", format= "pdf")
plt.show()
