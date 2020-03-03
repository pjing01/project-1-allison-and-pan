# Step Two of Project 1
# Allison and Pan

import math
import numpy as np
import MatPlotLib as mpl

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
    mpl.plot(periods, lengths)
    mpl.axis([0,100,0,100])
    mpl.show()
    