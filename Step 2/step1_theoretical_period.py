# Step Two of Project 1
# Allison and Pan

import matplotlib.pyplot as plt
import math
import numpy as np

lengths=[]
lengths_array=np.array(lengths)

## ***** UNITS ***** ##
def swing_period(lengths):
    periods=[]
    for i in range(len(lengths)):
        period=2*math.pi*math.sqrt(lengths[i]/9.8)
        periods.append(period)
    return periods
        
# **ask about what values should be on which axis
def graph_values(lengths,periods):
    plt.plot(periods, lengths)
    plt.axis([0,100,0,100])
    plt.show()
    
    