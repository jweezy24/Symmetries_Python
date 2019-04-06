import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
import matplotlib.pyplot as plt
def draw_cube():
    points = np.array([[-1, -1, -1],
                      [1, -1, -1 ],
                      [1, 1, -1],
                      [-1, 1, -1],
                      [-1, -1, 1],
                      [1, -1, 1 ],
                      [1, 1, 1],
                      [-1, 1, 1]])

    P = [[2.06498904e-01 , -6.30755443e-07 ,  1.07477548e-03],
     [1.61535574e-06 ,  1.18897198e-01 ,  7.85307721e-06],
     [7.08353661e-02 ,  4.48415767e-06 ,  2.05395893e-01]]

    Z = np.zeros((8,3))
    for i in range(8):
        Z[i,:] = np.dot(points[i,:],1)

    Z = 10.0*Z

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    r = [-1,1]

    X, Y = np.meshgrid(r, r)
    # plot vertices
    ax.scatter3D(Z[:, 0], Z[:, 1], Z[:, 2])

    # list of sides' polygons of figure
    verts = [[Z[0],Z[1],Z[2],Z[3]],
     [Z[4],Z[5],Z[6],Z[7]],
     [Z[0],Z[1],Z[5],Z[4]],
     [Z[2],Z[3],Z[7],Z[6]],
     [Z[1],Z[2],Z[6],Z[5]],
     [Z[4],Z[7],Z[3],Z[0]]]

    # plot sides
    ax.add_collection3d(Poly3DCollection(verts,
     facecolors='none', linewidths=1, edgecolors='r', alpha=.25))

    count = 1
    for (a, b, c) in Z:
        ax.text(a,b,c,chr(ord('a')+count))
        #ax.text(a,b,c,count)
        count+=1
    #uncomment the draw methods to see the lines
    draw_syms_edge(ax)
    draw_syms_verts(ax)
    draw_syms_face_pairs(ax)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()

def draw_syms_edge(ax):
    VecStart_x = [0,12,12,-12,0,12]
    VecStart_y = [12,0,12,0,-12,-12]
    VecStart_z = [12,12,0,12,12,0]
    VecEnd_x = [0,-12,-12,12,0,-12]
    VecEnd_y = [-12,0,-12,0,12,12]
    VecEnd_z  =[-12,-12,0,-12,-12,0]
    for i in range(6):
        ax.plot([VecStart_x[i], VecEnd_x[i]], [VecStart_y[i],VecEnd_y[i]],zs=[VecStart_z[i],VecEnd_z[i]])

def draw_syms_verts(ax):
    VecStart_x = [12,12,-12,-12]
    VecStart_y = [-12,12,-12,12]
    VecStart_z = [12,12,12,12]
    VecEnd_x = [-12,-12,12,12]
    VecEnd_y = [12,-12,12,-12]
    VecEnd_z  =[-12,-12,-12,-12]
    for i in range(4):
        ax.plot([VecStart_x[i], VecEnd_x[i]], [VecStart_y[i],VecEnd_y[i]],zs=[VecStart_z[i],VecEnd_z[i]])

def draw_syms_face_pairs(ax):
    VecStart_x = [12,0,0]
    VecStart_y = [0,12,0]
    VecStart_z = [0,0,12]
    VecEnd_x = [-12,0,0]
    VecEnd_y = [0,-12,0]
    VecEnd_z  =[0,0,-12]
    for i in range(3):
        ax.plot([VecStart_x[i], VecEnd_x[i]], [VecStart_y[i],VecEnd_y[i]],zs=[VecStart_z[i],VecEnd_z[i]])

draw_cube()
