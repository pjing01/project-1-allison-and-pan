# Step Two of Project 1
# Allison and Pan
# This file graphs the theoretical periods vs. lengths of  the pendulum
# We worked alone on this assignment

# IMPORT STATEMENTS
import matplotlib.pyplot as plt
import math
import numpy as np

# GLOBAL VARIABLES
lengths=[]
lengths_array=np.array(lengths)

# CUSTOM FUNCTIONS
def swing_period(lengths):
    # swing_period takes in an array of lengths as a parameter
    # returns an array of periods calculated for each length
    periods=[]
    for i in range(len(lengths)):
        period=2*math.pi*math.sqrt(lengths[i]/9.8)
        periods.append(period)
    periodarray=np.array(periods)
    return periodarray
        
def graph_values(lengths,periods):
    # graph_values takes an array of lengths and an array of periods as parameters
    # graphs length vs period for a theoretical model
    plt.plot(periods, lengths)
    plt.axis([0,100,0,100])
    plt.show()
    
    