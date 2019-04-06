import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
import matplotlib.pyplot as plt

def draw_octo():
    points = np.array([[-1, 0, 0],
                      [0, 0, 1 ],
                      [0, 1, 0],
                      [1, 0, 0],
                      [0, 0, -1 ],
                      [0, -1, 0]])


    Z = np.zeros((6,3))
    for i in range(6):
        Z[i,:] = np.dot(points[i,:],1)

    Z = 12.0*Z

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    r = [-1,1]

    X, Y = np.meshgrid(r, r)
    # plot vertices
    ax.scatter3D(Z[:, 0], Z[:, 1], Z[:, 2])

    # list of sides' polygons of figure
    verts = [[Z[0],Z[1],Z[5]],
     [Z[0],Z[1],Z[2]],
     [Z[0],Z[4],Z[5]],
     [Z[0],Z[4],Z[2]],
     [Z[2],Z[1],Z[3]],
     [Z[2],Z[4],Z[3]],
     [Z[3],Z[1],Z[5]],
     [Z[3],Z[4],Z[5]]]

    # plot sides
    ax.add_collection3d(Poly3DCollection(verts,
     facecolors='none', linewidths=1, edgecolors='r', alpha=.25))

    count = 1
    for (a, b, c) in Z:
        #ax.text(a,b,c,chr(ord('a')+count))
        ax.text(a,b,c,count)
        count+=1
    #comment out the draw methods to see specific forms of symmetry
    #draw_syms_edge(ax)
    #draw_syms_verts(ax)
    draw_syms_face_pairs(ax)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()

def draw_syms_edge(ax):
    VecStart_x = [6,6,6,-6,0,0]
    VecStart_y = [6,-6,0,0,-6,6]
    VecStart_z = [0,0,6,6,6,6]
    VecEnd_x = [-6,-6,-6,6,0,0]
    VecEnd_y = [-6,6,0,0,6,-6]
    VecEnd_z  =[0,0,-6,-6,-6,-6]
    for i in range(6):
        ax.plot([VecStart_x[i], VecEnd_x[i]], [VecStart_y[i],VecEnd_y[i]],zs=[VecStart_z[i],VecEnd_z[i]])

def draw_syms_verts(ax):
    VecStart_x = [12,0,0]
    VecStart_y = [0,0,12]
    VecStart_z = [0,12,0]
    VecEnd_x = [-12,0,0]
    VecEnd_y = [0,0,-12]
    VecEnd_z  =[0,-12,0]
    for i in range(3):
        ax.plot([VecStart_x[i], VecEnd_x[i]], [VecStart_y[i],VecEnd_y[i]],zs=[VecStart_z[i],VecEnd_z[i]])

def draw_syms_face_pairs(ax):
    VecStart_x = [4,4,4,-4]
    VecStart_y = [4,-4,4,4]
    VecStart_z = [4,4,-4,4]
    VecEnd_x = [-4,-4,-4,4]
    VecEnd_y = [-4,4,-4,-4]
    VecEnd_z  =[-4,-4,4,-4]
    for i in range(4):
        ax.plot([VecStart_x[i], VecEnd_x[i]], [VecStart_y[i],VecEnd_y[i]],zs=[VecStart_z[i],VecEnd_z[i]])

draw_octo()
