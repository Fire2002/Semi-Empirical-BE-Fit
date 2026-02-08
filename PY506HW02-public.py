# PY 506 HW 02 - Computational Activity

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd

"""
columns 1 - 6 of data file:
Mass number, number of protons, name of isotope, mass [MeV/c^2],
binding energy [MeV], binding energy per nucleus [MeV]
"""

# read BE-per-nucleon data: PY506HW02data.txt
data = pd.read_csv('<insert path to data file here>', sep = " ", header = None)

col1, col2 = data[0], data[1]
col3, col4 = data[2], data[3]
col5, col6 = data[4], data[5]
x1data, y1data = col1, col6 # mass number, BE per nucleus [MeV]

def BE_formula(A,Z,a_v,a_s,a_c,a_symm):
        return a_v*A - a_s*A**(2/3)-a_c*Z*(Z-1)*A**(-1/3)-a_symm*((A-2*Z)**2)/A

A = np.linspace(0.000001,265,25)
popt, pcov = curve_fit(BE_formula,x1data,y1data, maxfev = 5000)
av_fit, az_fit = popt[0], popt[1]
ac_fit, a_symm_fit = popt[2], popt[3]

def graphing():
    plt.close()
    plt.title('Binding energy per nucleus [MeV] vs Mass number ')
    plt.plot(x1data,BE_formula(x1data,*popt),label="Fitted Curve", color = 'b') # FITTING PLOT
    plt.plot(col1,col6,".", label="Given data",color = 'mediumblue', alpha = 0.25) # DATA PLOT
    plt.xlabel('Mass number')
    plt.ylabel('Binding energy per nucleus [MeV]')
    plt.xticks(np.arange(0,265,25))
    plt.yticks(np.arange(0,10,1))
    plt.ylim(0,9)
    plt.legend()
    plt.show()

graphing()
print(av_fit, az_fit, ac_fit, a_symm_fit)








