# IMPORT STATEMENTS
import os
import numpy as np
import math
import matplotlib.pyplot as plt
import scipy.signal as sig

# GLOBAL VARIABLES
# path = "/Users/allisoncremer/Documents/GitHub/project-1-allison-and-pan/Step 3"
path = "/Users/panru/Documents/Github/project-1-allison-and-pan/Step 3"

# CUSTON FUNCTIONS
def create_acceleration_array(fin):
    array = np.loadtxt(fin, delimiter=',')
    return array

def create_acceleration_lists(arr):
    timelist=[]
    xlist=[]
    ylist=[]
    zlist=[]
    for lst in arr:
        timelist.append(lst[0])
    for lst in arr:
        xlist.append(lst[1])
    for lst in arr:
        ylist.append(lst[2])
    for lst in arr:
        zlist.append(lst[3])
    return create_acceleration_graph(timelist, xlist, ylist, zlist)

def create_acceleration_graph(timelist, xlist, ylist, zlist):
    fig, (ax1, ax2, ax3) = plt.subplots(3, sharex=True, figsize=(15,10))
    fig.suptitle('Acceleration vs. Time')
    ax1.set_title('X-axis')
    ax1.plot(timelist, xlist)
    ax2.set_title('Y-axis')
    ax2.plot(timelist, ylist)
    ax3.set_title('Z-axis')
    ax3.plot(timelist, zlist)
    
def create_angle_array(arr):
    timelist=[]
    thetalist=[]
    array=[]
    for info in arr:
        denom=math.sqrt(info[2]*info[2]+info[3]*info[3])
        num=info[1]
        timelist.append(info[0])
        thetalist.append(math.atan2(num,denom))
    array=np.array([timelist,thetalist])
    return array

def create_angle_graph(arr):
    plt.figure(2, figsize=(15,10))
    plt.title('Pendulum Angle vs. Time')
    plt.plot(arr[0],arr[1])
    plt.axis(xmin=0,xmax=20000,ymin=-.1,ymax=.1)
    plt.show()
    
def find_period(arr):
    time = np.array(arr[0])
    y = np.array(arr[1])
    y_filt = sig.medfilt(y)
    y_pks, _ = sig.find_peaks(y)
    y_filt_pks, _ = sig.find_peaks(y_filt)
    plt.figure(3, figsize=(15,10))
    plt.subplot(2,2,1)
    plt.plot(time, y, 'r-', time[y_pks], y[y_pks], 'b.')
    plt.title('Original')
    plt.subplot(2,2,3)
    plt.plot(time, y_filt, 'r-', time[y_filt_pks], y_filt[y_filt_pks], 'b.')
    plt.title('Original Median Filtered')
    plt.tight_layout()
    plt.show()
    
    
# MAIN
os.chdir(path)
data_files = ['24.5cm.csv', '30cm.csv', '35cm.csv', '41cm.csv', '46cm.csv']
for length_file in data_files:
    print('\n\n' + length_file + ':')
    newarr=create_acceleration_array(length_file)
    create_acceleration_lists(newarr)
    otherarr=create_angle_array(newarr)
    find_period(otherarr)
