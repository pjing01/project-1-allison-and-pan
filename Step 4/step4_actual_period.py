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
    array=[]
    for info in arr:
        denom=math.sqrt(info[2]*info[2]+info[3]*info[3])
        num=info[1]
        templist=[info[0],math.atan2(num,denom)]
        array=np.append(array,templist)
    return array



# MAIN
os.chdir(path)
newarr=create_acceleration_array('35cm.csv')
otherarr=create_angle_array(newarr)

