#parser for wrls
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import re
holder = []
with open("biaugmented_truncated_cube_(J67).wrl", "r") as vrml:
    for lines in vrml:
        a = re.findall("[-0-9]{1,3}.[0-9]{6}", lines)
        if len(a) == 3:
            holder.append((float, a))
print(holder)
new_holder = []
for i in holder:
    print(i[1])
    new_holder.append([float(i[1][0]),float(i[1][1]),float(i[1][2])])
holder_array = np.array(new_holder) #if you want numpy array

#3D Plotting
x,y,z = zip(*new_holder)
fig = plt.figure()
ax = Axes3D(fig)
ax.plot(x,y,z)
plt.show()
