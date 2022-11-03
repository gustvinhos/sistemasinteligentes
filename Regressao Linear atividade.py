import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
import math
import pandas as pd

# Read the data from file "PM e Volume.csv"
x = [1,2,3,4,5,6]
y = [80.5,81.6,82.1,83.7,83.9,85.0]


#calculate the correlation between the two variables
print(pearsonr(x,y))

#build the graph of reta of the correlation 
plt.scatter(x,y)
plt.show()

#predict the value of y when the value of x is 5.5
print(5.5*0.2+80.5)






