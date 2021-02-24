import numpy as np
import scipy.special as sp
from math import factorial

import matplotlib.pyplot as plt

def radial(r,n,l):
    # Eq. 81
    N = np.sqrt(factorial(n-l-1)/(2*n*factorial(n+l)))*(2/(n*a))**(l+1.5)
    exp = np.exp(-r/(n*a))
    lag = sp.assoc_laguerre(2*r/(n*a),n-l-1,2*l+1)

    return N*r**l*exp*lag

hbar = 6.62607015e-34/(2*np.pi) # J.s
e = 1.60217662e-19 # C
me = 9.10938356e-31 # kg
mp = 1.6726219e-27 # kg
epsilon = 8.85418782e-12 # F.m-1
a = 4*np.pi*epsilon*hbar**2/(me*e**2) # m

if __name__=="__main__":

    step = a/5000
    R = np.arange(0,20*a,step)

    d = dict({1:"s",2:"p",3:"d"})

    R10 = radial(R,1,0)
    R20 = radial(R,2,0)
    R21 = radial(R,2,1)
    R30 = radial(R,3,0)
    R31 = radial(R,3,1)
    R32 = radial(R,3,2)

    B = 0.
    for i in range(len(R)):
        B = B + R[i]**2*R10[i]**2*step

    fig, axes = plt.subplots(3,2,sharex=True)

    for i in range(4):
        for k in range(i):
            axes[i-1][0].plot(R/a,radial(R,i,k)*a**(3/2),label="%i%s"%(i,d[k+1]))
            axes[i-1][1].plot(R/a,a*R**2*np.abs(radial(R,i,k))**2)
            axes[i-1][0].legend()
            axes[i-1][0].set_ylabel("$R_{n,l}(r)\\times a_\mu^{3/2}$")
            axes[i-1][1].set_ylabel("$r^2 |R_{n,l}(r)|^2 \\times a_\mu$")
            axes[i-1][0].axhline(color='black',linewidth=0.5)
            axes[i-1][1].axhline(color='black',linewidth=0.5)
            if(i-1==0):
                axes[i-1][0].set_title("Radial function")
                axes[i-1][1].set_title("Probability density")
            if(i-1==2):
                axes[i-1][0].set_xlabel("$r/a_\mu$")
                axes[i-1][1].set_xlabel("$r/a_\mu$")

    plt.tight_layout()
    plt.show()
#   plt.savefig("radial_function.png")



