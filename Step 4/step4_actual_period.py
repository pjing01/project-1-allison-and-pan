# IMPORT STATEMENTS
import os
import numpy as np
import math
import matplotlib.pyplot as plt

# GLOBAL VARIABLES
path = "/Users/allisoncremer/Documents/GitHub/project-1-allison-and-pan/Step 3"

# CUSTON FUNCTIONS
def create_acceleration_array(fin):
    array = np.loadtxt(fin, delimiter=',')
    print(array)
    return array


def create_angle_array(arr):
    timelist=[]
    thetalist=[]
    array=[]
    for info in arr:
        denom=math.sqrt(info[2]*info[2]+info[3]*info[3])
        num=info[1]
        timelist.append(info[0])
        thetalist.append(math.atan2(num,denom))
    array=[timelist,thetalist]
    return array



# MAIN
os.chdir(path)
newarr=create_acceleration_array('30cm.csv')
otherarr=create_angle_array(newarr)
timelist=[]
xlist=[]
ylist=[]
zlist=[]

for lst in newarr:
    timelist.append(lst[0])
for lst in newarr:
    xlist.append(lst[1])
for lst in newarr:
    ylist.append(lst[2])
for lst in newarr:
    zlist.append(lst[3])

plt.plot(timelist,xlist)
plt.show()
plt.plot(timelist,ylist)
plt.show()
plt.plot(timelist,zlist)
plt.show()
    

# HOW TO MAKE THETA GRAPHS
#plt.plot(otherarr[0],otherarr[1])
#plt.axis(xmin=0,xmax=20000,ymin=-.1,ymax=.1)
#plt.show()
