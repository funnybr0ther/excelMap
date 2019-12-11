from numpy import *
import matplotlib.pyplot as plt
from matplotlib import rc

rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica']})
# for Palatino and other serif fonts use:
# rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)

R = 8.314
F = 96500
T = 298

V_min = 1.23

pH = linspace(0, 14, 1000)
acid_pH_reduction = R * T / F * (-pH) / log10(e)
acid_pH_oxydation = 1.23 + R * T / F * (-pH) / log10(e)
basic_pH_reduction = 0.40 + R * T / F * (14 - pH) / log10(e)
basic_pH_oxydation = -0.822 + R * T / F * (14 - pH) / log10(e)

fig, ax = plt.subplots(figsize=(6, 4), tight_layout=True)
ax.plot(pH, acid_pH_oxydation)
ax.plot(pH, basic_pH_oxydation)
ax.plot(pH, basic_pH_reduction)
ax.plot(pH, acid_pH_reduction)

ax.set_xlabel(r'$pH$')
ax.set_ylabel(r'$E_{eq}$')
plt.savefig("oui.pdf",format="pdf")
plt.show()



