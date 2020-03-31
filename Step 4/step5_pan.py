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
    velNext = vel+acc
    posNext = pos+vel
    accNext = -1*gravity*math.sin(pos)
    return posNext,velNext,accNext

def print_system(time,pos,vel,acc):
    print("TIME:         ", time)
    print("POSITION:     ", pos)
    print("VELOCITY:     ", vel)
    print("ACCELERATION: ", acc, "\n")

def create_graph(time, pos, vel, acc):
    fig, (ax1, ax2, ax3) = plt.subplots(3, sharex=True, figsize=(15,10))
    fig.suptitle('Pendulum')
    ax1.set_title('Position')
    ax1.plot(time, pos)
    ax2.set_title('Velocity')
    ax2.plot(time, vel)
    ax3.set_title('Acceleration')
    ax3.plot(time, acc)

#MAIN
# initial conditions
pos = [(math.pi/2)]
vel = [0]
acc = [0]
time = np.linspace(0,20,201)
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

create_graph(time, pos, vel, acc)