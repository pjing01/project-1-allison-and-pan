# IMPORT STATEMENTS
import os
import numpy as np

# GLOBAL VARIABLES
path = "/Users/allisoncremer/Documents/GitHub/project-1-allison-and-pan/Step 3"

# CUSTON FUNCTIONS
def create_array(fin):
    arr = np.array([])
    for ln in fin:
        newrow=[ln]
        np.append(arr,newrow)
    return arr



# MAIN
os.chdir(path)
fin=open("dataexample.pdf","r",encoding='utf-8')
print(create_array(fin))