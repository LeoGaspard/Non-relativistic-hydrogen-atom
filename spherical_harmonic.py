import numpy as np
import scipy.special as sp
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def sph2cart(r,theta,phi):
    X = r*np.sin(theta)*np.cos(phi)
    Y = r*np.sin(theta)*np.sin(phi)
    Z = r*np.cos(theta)

    return X,Y,Z

def Ylm(l,m,theta,phi):
    n = np.sqrt((2*l+1)/(4*np.pi) * (np.math.factorial(l-np.abs(m)))/(np.math.factorial(l+np.abs(m)))) # Eq. 36

    leg = sp.lpmv(np.abs(m),l,np.cos(theta))

    exp = np.exp(complex(0,1)*m*phi)

    return n*leg*exp


if __name__ == "__main__":

    theta = np.arange(0,np.pi+np.pi/50,np.pi/50)
    phi = np.arange(0,2*np.pi+np.pi/50, np.pi/50)

    theta, phi = np.meshgrid(theta,phi)

    fig = make_subplots(rows=3,cols=5,specs=[[{'type':'surface'},{'type':'surface'},{'type':'surface'},{'type':'surface'},{'type':'surface'}]
        ,[{'type':'surface'},{'type':'surface'},{'type':'surface'},{'type':'surface'},{'type':'surface'}]
        ,[{'type':'surface'},{'type':'surface'},{'type':'surface'},{'type':'surface'},{'type':'surface'}]])

    for l in [0,1,2]:
        for m in range(-l,l+1):
            Yl = Ylm(l,m,theta,phi)
            X,Y,Z = sph2cart(np.abs(Yl)**2,theta,phi)
            fig.add_trace(go.Surface(x=X,y=Y,z=Z,colorscale='HSV',colorbar={"title":"Phase"},surfacecolor=np.angle(Yl),showscale=True, cmax=np.pi, cmin=-np.pi, cmid = 0,meta="$Y_{%i}^{%i}$"%(l,m)),row=l+1,col=m+3)

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

    fig.write_html("complex_spherical_harmonics.html")
