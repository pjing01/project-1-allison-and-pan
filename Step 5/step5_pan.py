# IMPORT STATEMENTS
import numpy as np
import math
import matplotlib.pyplot as plt
#import scipy.signal as sig

# GLOBAL VARIABLES
gravity = 9.8

# CUSTOM FUNCTIONS
def update_system(acc,pos,vel,time1,time2):
    # position and velocity update below
    dt = time2-time1
    velNext = vel+acc*dt
    posNext = pos+vel*dt
    accNext = -1*(gravity/.35)*math.sin(pos)
    return posNext,velNext,accNext

def print_system(time,pos,vel,acc):
    print("TIME:         ", time)
    print("POSITION:     ", pos)
    print("VELOCITY:     ", vel)
    print("ACCELERATION: ", acc, "\n")

def create_graph(time, pos, vel, acc):
    fig, (ax1, ax2, ax3) = plt.subplots(3, sharex=True, figsize=(15,10))
    fig.suptitle('Pendulum')
    ax1.set_title('Position vs. Time')
    ax1.plot(time, pos)
    ax2.set_title('Velocity vs. Time')
    ax2.plot(time, vel)
    ax3.set_title('Acceleration vs. Time')
    ax3.plot(time, acc)
    
def find_peaks(arr):
    time = np.array(arr[0])
    y = np.array(arr[1])
    y_filt = sig.medfilt(y)
    y_pks, _ = sig.find_peaks(y)
    y_filt_pks, _ = sig.find_peaks(y_filt)
    return time, y, y_filt

def create_peak_graph(time, y, y_filt):
    plt.figure(3, figsize=(15,10))
    plt.subplot(2,2,1)
    plt.plot(time, y, 'r-', time[y_pks], y[y_pks], 'b.')
    plt.title('Original')
    plt.subplot(2,2,3)
    plt.plot(time, y_filt, 'r-', time[y_filt_pks], y_filt[y_filt_pks], 'b.')
    plt.title('Original Median Filtered')
    plt.tight_layout()
    plt.show()

#MAIN
# initial conditions
pos = [(math.pi*2/3)]
vel = [0]
acc = [0]
time = np.linspace(0,15,15001)
print_system(time[0],pos[0],vel[0],acc[0])

i = 1
while i < len(time):
    # update position and velocity using previous values and time step
    posNext, velNext, accNext = update_system(acc[i-1],pos[i-1],vel[i-1],time[i-1],time[i])
    pos.append(posNext)
    vel.append(velNext)
    acc.append(accNext)
    print_system(time[i],pos[i],vel[i], acc[i])
    i += 1

#create_graph(time, pos, vel, acc)

plt.subplot(3,1,1)
plt.plot(time, pos, 'ro--') 

plt.xlabel('Time (seconds)')
plt.ylabel('Position (m)')
plt.title('Position vs Time')
plt.xlim((0, 15)) # set x range to -1 to 8
plt.grid()


plt.subplot(3,1,2)
plt.plot(time, vel, 'ro--') 
plt.xlabel('Time (seconds)')
plt.ylabel('Velocity (m/s)')
plt.title('Velocity vs Time')
plt.xlim((0, 15)) # set x range to -1 to 8
plt.grid()


plt.subplot(3,1,3)
plt.plot(time, acc, 'ro--') 
plt.xlabel('Time (seconds)')
plt.ylabel('Acceleration (m/s^2)')
plt.title('Acceleration vs Time')
plt.xlim((0, 15)) # set x range to -1 to 8
plt.grid()
plt.tight_layout()
plt.show()