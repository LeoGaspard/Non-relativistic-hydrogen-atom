import numpy as np
import math
import scipy.special as sp
import matplotlib.pyplot as plt

def sph2cart(r,theta,phi):
    X = r*np.sin(theta)*np.cos(phi)
    Y = r*np.sin(theta)*np.sin(phi)
    Z = r*np.cos(theta)

    return X,Y,Z

def Ylm(l,m,theta,phi):
    n = np.sqrt((2*l+1)/(4*np.pi) * (math.factorial(l-np.abs(m)))/(math.factorial(l+np.abs(m)))) # Eq. 36

    leg = sp.lpmv(np.abs(m),l,np.cos(theta))

    exp = np.exp(complex(0,1)*m*phi)

    return n*leg*exp


if __name__ == "__main__":

    theta = np.arange(0,np.pi+np.pi/50,np.pi/50)
    phi = np.arange(0,2*np.pi+np.pi/50, np.pi/50)
    theta, phi = np.meshgrid(theta,phi)
    fig, ax = plt.subplots(nrows=3, ncols=5, subplot_kw={'projection': '3d'}, figsize=(10, 10))
    for l in [0,1,2]:
        for m in range(-l,l+1):
            Yl = Ylm(l,m,theta,phi)
            X,Y,Z = sph2cart(np.abs(Yl)**2,theta,phi)
            surf = ax[l, l+m + 2 - l].plot_surface(X, Y, Z, cmap="coolwarm")

    for i in ax.flatten():
        i.set_xticks([])
        i.set_yticks([])
        i.set_zticks([])
        i.xaxis.set_pane_color((1,1,1,0))
        i.yaxis.set_pane_color((1,1,1,0))
        i.zaxis.set_pane_color((1,1,1,0))
        i.set_axis_off()

    for i in range(5):
        ax[0,i].set_title(f"{i-2:2.0f}", fontsize="20", weight="bold")

    fig.text(0.05, 0.82, "0", fontsize="20", weight="bold")
    fig.text(0.05, 0.52, "1", fontsize="20", weight="bold")
    fig.text(0.05, 0.22, "2", fontsize="20", weight="bold")

    fig.text(0.5, 0.95, "m", fontsize="20", weight="bold")
    fig.text(0.01, 0.5, "l", fontsize="20", weight="bold")


    fig.subplots_adjust(top=0.95, bottom=0.1, left=0.1, right=0.95, wspace=0.00, hspace=0.00)

    plt.savefig("/home/leogaspard/Documents/Code/leogaspard.github.io/assets/complex_spherical_harmonics.png", transparent=True)
