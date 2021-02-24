import numpy as np
import scipy.special as sp
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from spherical_harmonic import *

def Ylmr(l,m,theta,phi):
    if(m > 0):
        return np.real((-1)**m/np.sqrt(2)*(Ylm(l,m,theta,phi) + np.conjugate(Ylm(l,m,theta,phi))))
    elif(m == 0):
        return np.real(Ylm(l,m,theta,phi))
    elif(m < 0):
        return np.real((-1)**m/(complex(0,1)*np.sqrt(2))*(Ylm(l,-m,theta,phi) - np.conjugate(Ylm(l,-m,theta,phi))))

if __name__ == "__main__":

    theta = np.arange(0,np.pi+np.pi/50,np.pi/50)
    phi = np.arange(0,2*np.pi+np.pi/50, np.pi/50)

    theta, phi = np.meshgrid(theta,phi)

    fig = make_subplots(rows=3,cols=5,specs=[[{'type':'surface'},{'type':'surface'},{'type':'surface'},{'type':'surface'},{'type':'surface'}]
        ,[{'type':'surface'},{'type':'surface'},{'type':'surface'},{'type':'surface'},{'type':'surface'}]
        ,[{'type':'surface'},{'type':'surface'},{'type':'surface'},{'type':'surface'},{'type':'surface'}]])

    for l in [0,1,2]:
        for m in range(-l,l+1):
            Yl = Ylmr(l,m,theta,phi)
            X,Y,Z = sph2cart(np.abs(Yl)**2,theta,phi)
            fig.add_trace(go.Surface(x=X,y=Y,z=Z,colorscale='Picnic',surfacecolor=((np.real(Yl)<0)*(-1)+(np.real(Yl)>0)*1),colorbar={"title":"Sign"},showscale=True,cmid = 0,meta="$Y_{%i}^{%i}$"%(l,m)),row=l+1,col=m+3)

    fig.update_layout(scene3_aspectmode='cube')
    fig.update_layout(scene7_aspectmode='cube')
    fig.update_layout(scene8_aspectmode='cube')
    fig.update_layout(scene9_aspectmode='cube')
    fig.update_layout(scene11_aspectmode='cube')
    fig.update_layout(scene12_aspectmode='cube')
    fig.update_layout(scene13_aspectmode='cube')
    fig.update_layout(scene14_aspectmode='cube')
    fig.update_layout(scene15_aspectmode='cube')
    fig.update_scenes(xaxis=dict({'visible':False}),yaxis=dict({'visible':False}),zaxis=dict({'visible':False}))
    fig.show()

    fig.write_html("real_spherical_harmonics.html")
    fig.write_image("real_spherical_harmonics.png")
