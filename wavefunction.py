from radial_function import *
from real_spherical_harmonic import *

import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import sys
import os

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 3, length = 100, fill = '\u2588'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)

    print('\r%30s |%s| %7s%% %s ' % (prefix, bar, percent, suffix),end='\r')
    # Print New Line on Complete
    if iteration == total:
        print()

def WF(n,l,m,r,theta,phi):
    rad = radial(r,n,l)
    ang = Ylmr(l,m,theta,phi)

    return rad*ang

def update():
    print('hi')


if __name__=="__main__":

    n = int(sys.argv[1])
    l = int(sys.argv[2])
    m = int(sys.argv[3])
    maxpoints = int(sys.argv[4])
    rmax = float(sys.argv[5])

    orbname = dict({0:"s",1:"p",2:"d",3:"f",4:"g",5:"h"})

    red_points = [[],[],[]]
    blue_points = [[],[],[]]

    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")


    ax.set_title("Orbital : %i%s$_{%i}$"%(n,orbname[l],m))

    npoints = 0
    ntest = 1

    X = []
    Y = []
    Z = []
    c = []

    maxaccep = 0.0

    while npoints < maxpoints:
        ntest = ntest+1
      # r = np.random.rand()*rmax*a
      # theta = np.random.rand()*np.pi
      # phi = np.random.rand()*2*np.pi

        x = np.random.rand()*rmax*a*2-rmax*a
        y = np.random.rand()*rmax*a*2-rmax*a
        z = np.random.rand()*rmax*a*2-rmax*a

        r = np.sqrt(x**2+y**2+z**2)
        theta = np.arccos(z/r)
        phi = np.arctan(y/x)

        v = WF(n,l,m,r,theta,phi)

        p = v**2*r**2*np.sin(theta)*a

        if p > maxaccep:
            maxaccep = p

        t = np.random.rand()

        if p>t:
         #  x,y,z = sph2cart(r,theta,phi)
            X.append(x)
            Y.append(y)
            Z.append(z)
            c.append((v<0)*(-1)+(v>0)*1)
            npoints += 1
            printProgressBar(npoints,maxpoints, prefix = '', suffix = '', decimals = 3, length = 100, fill = '\u2588')

    ax.set_xlim3d([np.min(X),np.max(X)])
    ax.set_ylim3d([np.min(Y),np.max(Y)])
    ax.set_zlim3d([np.min(Z),np.max(Z)])
    ax.set_xlabel('x (m)',size=20)
    ax.set_ylabel('y (m)',size=20)
    ax.set_zlabel('z (m)',size=20)
    ax.set_title('Real orbital : %i%s$_%i$'%(n,orbname[l],m),size=20)
    p = ax.scatter(X,Y,Z,c=c,s=2,cmap='bwr')
    fig.tight_layout()
#   c = fig.colorbar(p,ax=ax)
#   c.ax.set_ylabel("Sign of $\Psi$")

    print(maxaccep)

    plt.show()
