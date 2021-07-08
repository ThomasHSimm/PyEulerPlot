# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 12:19:02 2021

@author: 44781
"""
import matplotlib.pyplot as plt
import numpy as np

def plotCube(xx,self):

    
    
    AL=.7
    print(AL)
    
    
    print('Problem here')
    
    plt.close('plotcube')
    
    
    ax = plt.figure(num='plotcube').add_subplot(projection='3d')
    
    # fig=self.canvas.figure.figure
    # ax = fig.add_subplot(projection='3d')
    # ax=self.fig.add_subplot(projection='3d')
    
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    # Plot the surface with face colors taken from the array we made.
    surf = ax.plot_surface(xx['Xbot'], xx['Ybot'], xx['Zbot'],  linewidth=0,alpha=AL)
    surf = ax.plot_surface(xx['Xtop'], xx['Ytop'], xx['Ztop'],  linewidth=0,alpha=AL)
    surf = ax.plot_surface(xx['Xleft'], xx['Yleft'], xx['Zleft'],  linewidth=0,alpha=AL)
    surf = ax.plot_surface(xx['Xright'], xx['Yright'], xx['Zright'],  linewidth=0,alpha=AL)
    surf = ax.plot_surface(xx['Xfront'], xx['Yfront'], xx['Zfront'],  linewidth=0,alpha=AL)
    surf = ax.plot_surface(xx['Xback'], xx['Yback'], xx['Zback'],  linewidth=0,alpha=AL)

    #ax.set_aspect('equal')
    ax.view_init(azim=30)
    #ax.set_axis_off()
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])
    # ax.set_xlim([-1,1])
    # ax.set_ylim([-1,1])
    # ax.set_zlim([-1,1])
    
def gmatrix(phi1,PHI,phi2):
    import numpy as np
    phi1=phi1*np.pi/180
    PHI=PHI*np.pi/180
    phi2=phi2*np.pi/180    

    g=np.array([[np.cos(phi1)*np.cos(phi2)-np.sin(phi1)*np.sin(phi2)*np.cos(PHI),	np.sin(phi1)*np.cos(phi2)+np.cos(phi1)*np.sin(phi2)*np.cos(PHI),	np.sin(phi2)*np.sin(PHI)],
                [-np.cos(phi1)*np.sin(phi2)-np.sin(phi1)*np.cos(phi2)*np.cos(PHI),	-np.sin(phi1)*np.sin(phi2)+np.cos(phi1)*np.cos(phi2)*np.cos(PHI),np.cos(phi2)*np.sin(PHI)],
                [np.sin(phi1)*np.sin(PHI),	-np.cos(phi1)*np.sin(PHI),	np.cos(PHI)]])
    return g

def rotateG(g):
    #vectors for corner of cube    
    XYZ=np.array([[0.0,1.0,1.0],#0 a
                  [0.0,0.0,1.0],#1 b
                  [1.0,0.0,1.0],#2 c
                  [1.0,1.0,1.0],#3 d
                  [1.0,1.0,0.0],#4 e
                  [1.0,0.0,0.0],#5 f
                  [0.0,0.0,0.0],#6 g
                  [0.0,1.0,0.0]])#7 h
    
    # rotate vectors by g
    XYZ2=XYZ
    i=0
    for rows in XYZ:
        #print(i)
        #print(rows)
        #print(g.dot(rows))
        XYZ2[i,:]=g.dot(rows)
        #print(XYZ2[i,:])
        #print("----------")
        i+=1
    
    # different planes of cube               
    # planebot=efgh 4567
    Xbot=np.array([[XYZ[4,0],XYZ[5,0]],
                   [XYZ[7,0],XYZ[6,0]]])
    Ybot=np.array([[XYZ[4,1],XYZ[5,1]],
                   [XYZ[7,1],XYZ[6,1]]])
    Zbot=np.array([[XYZ[4,2],XYZ[5,2]],
                   [XYZ[7,2],XYZ[6,2]]])
    # planetop=abcd 0123
    Xtop=np.array([[XYZ[0,0],XYZ[1,0]],
                   [XYZ[3,0],XYZ[2,0]]])
    Ytop=np.array([[XYZ[0,1],XYZ[1,1]],
                   [XYZ[3,1],XYZ[2,1]]])
    Ztop=np.array([[XYZ[0,2],XYZ[1,2]],
                   [XYZ[3,2],XYZ[2,2]]])
    # planeLHS=adeh 0347
    Xleft=np.array([[XYZ[0,0],XYZ[3,0]],
                   [XYZ[7,0],XYZ[4,0]]])
    Yleft=np.array([[XYZ[0,1],XYZ[3,1]],
                   [XYZ[7,1],XYZ[4,1]]])
    Zleft=np.array([[XYZ[0,2],XYZ[3,2]],
                   [XYZ[7,2],XYZ[4,2]]])
    # planeRHS=bcfg 1256
    Xright=np.array([[XYZ[1,0],XYZ[2,0]],
                   [XYZ[6,0],XYZ[5,0]]])
    Yright=np.array([[XYZ[1,1],XYZ[2,1]],
                   [XYZ[6,1],XYZ[5,1]]])
    Zright=np.array([[XYZ[1,2],XYZ[2,2]],
                   [XYZ[6,2],XYZ[5,2]]])
    # planefront=cdef 2345
    Xfront=np.array([[XYZ[2,0],XYZ[3,0]],
                   [XYZ[5,0],XYZ[4,0]]])
    Yfront=np.array([[XYZ[2,1],XYZ[3,1]],
                   [XYZ[5,1],XYZ[4,1]]])
    Zfront=np.array([[XYZ[2,2],XYZ[3,2]],
                   [XYZ[5,2],XYZ[4,2]]])
    # planeback=abgh 0167
    Xback=np.array([[XYZ[0,0],XYZ[1,0]],
                   [XYZ[7,0],XYZ[6,0]]])
    Yback=np.array([[XYZ[0,1],XYZ[1,1]],
                   [XYZ[7,1],XYZ[6,1]]])
    Zback=np.array([[XYZ[0,2],XYZ[1,2]],
                   [XYZ[7,2],XYZ[6,2]]])
    
    # create dictionary to export data
    XYZ2=dict([('Xbot',Xbot), ('Ybot',Ybot), ('Zbot',Zbot),
               ('Xtop',Xtop),('Ytop',Ytop),('Ztop',Ztop),
               ('Xleft',Xleft),('Yleft',Yleft),('Zleft',Zleft),
               ('Xright',Xright),('Yright',Yright),('Zright',Zright),
               ('Xfront',Xfront),('Yfront',Yfront),('Zfront',Zfront),
               ('Xback',Xback),('Yback',Yback),('Zback',Zback)])
    
    return XYZ2

# phi1=0.0
# PHI=30.0
# phi2=30.0     
# g=gmatrix(phi1,PHI,phi2)     
# XYZ2=rotateG(g)
# plotCube(XYZ2)

# # x=np.array([0 ,1 ,1 ,0 ,0 ,0 ,0 ,0])
# # y=np.array([0 ,0 ,1 ,1 ,1 ,1 ,0 ,0])
# # z=np.array([0 ,0 ,0 ,0 ,0 ,1 ,1 ,0])
# # ax2 = plt.figure().add_subplot(projection='3d')
# # ax2.set_xlabel('x')
# # ax2.set_ylabel('y')
# # ax2.set_zlabel('z')
# # # Plot the surface with face colors taken from the array we made.
# # surf = ax2.plot3D(x,y,z)

# # ax2.view_init(azim=30)
