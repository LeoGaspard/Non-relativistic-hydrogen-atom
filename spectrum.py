import numpy as np
from numpy import pi

import matplotlib.pyplot as plt

import matplotlib as mpl
from cycler import cycler

yellow = "#E8F086"
green  = "#6FDE64"
red    = "#FF4242"
purple = "#A020F0"
blue   = "#235FA4"
marine = "#0A284B"
orange = "#FF934F"
sand   = "#E1DAAE"
cyan   = "#058ED9"

mpl.rcParams['font.size'] = 20
mpl.rcParams['axes.prop_cycle'] = cycler('color', [blue, red, green, orange, purple, yellow, marine, sand, cyan])


def E(n):
    return fac/(n**2)

def E_to_nm(E):
    return 1e9*hbar*2*pi*c/E

def nm_to_rgb(nm):
    if nm >= 380 and nm <= 440:
        attenuation = 0.3 + 0.7 * (nm-380)/(440-380)
        R = -(nm-440)/(440-380)*attenuation
        G = 0.0
        B = attenuation
    elif nm >= 440 and nm <= 490:
        R = 0.0
        G = (nm-440)/(490-440)
        B = 1.0
    elif nm >= 490 and nm <= 510:
        R = 0.0
        G = 1.0
        B = -(nm-510)/(510-490)
    elif nm >= 510 and nm <= 580:
        R = (nm-510)/(580-510)
        G = 1.0
        B = 0.0
    elif nm >= 580 and nm <= 645:
        R = 1.0
        G = -(nm-645)/(645-580)
        B = 0.0
    elif nm >= 645 and nm <= 750:
        attenuation = 0.3 + 0.7* (750 - nm)/(750 - 645)
        R = attenuation
        G = 0.0
        B = 0.0
    else:
        R = 0.0
        G = 0.0
        B = 0.0

    print(nm, R, G, B)

    return (R,G,B)

c = 299792458
me = 9.10938356e-31 # kg
mp = 1.6726219e-27 # kg
e = 1.60217662e-19 # C
epsilon = 8.85418782e-12 # F.m-1
hbar = 1.054571817e-34 # J.s

mu = (me*mp)/(me+mp)

j_to_ev = 6.241509e18

fac = -mu*e**4/(32*pi**2*epsilon**2*hbar**2)


fig, ax = plt.subplots()

count = 0

for i in range(1,8):
    for j in range(8,i,-1):
        nm = E_to_nm(E(j)-E(i))
        ax.plot([nm,nm],[0,100],color=nm_to_rgb(nm))
        count = count + 5

ax.set_yticks([])
ax.set_xlabel("Wavelength (nm)",size=20)

ax.set_xscale("log")
ax.set_title("The hydrogen spectral series",size=20)

fig.tight_layout()
plt.savefig("/home/leogaspard/Documents/Code/leogaspard.github.io/assets/spectral_series.png")
