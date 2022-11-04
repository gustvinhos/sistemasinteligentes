import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
import math
import pandas as pd

# Read the data from file "PM e Volume.csv"
x = [6,8,6,10,8,14,12,14,12,16]
y = [8,8,12,12,16,16,20,20,24,24]


#calculate the correlation coefficient
b,_ = pearsonr(x, y)
print('Pearsons correlation: %.3f' % b)

a = (sum(y)-(b*sum(x)))/len(x)
print(a)

significancePercentage = 0.05
significance = a + b*significancePercentage
print(significance)















