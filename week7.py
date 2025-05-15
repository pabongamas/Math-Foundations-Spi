# onfidence interval for popula�on mean – When the popula�on standard devia�on (𝝈𝝈) is known. 
# Use the data below to calculate a confidence interval for the true popula�on mean �me (in minutes) 
# students take to commute to College, using a sample of 39 students. Assume the popula�on 
# standard devia�on is known to be 5.6 minutes. 
# 12, 12, 13, 13, 15, 16, 17, 22, 23, 25, 26, 27, 28, 28, 29, 17, 22, 23, 25, 26, 27, 28, 28, 29, 13, 15, 16, 
# 17, 22, 23, 25, 26, 27, 28, 28, 29, 17, 22, 23 
import numpy as np
from scipy.stats import norm

#sample data
x=np.array([12, 12, 13, 13, 15, 16, 17, 22, 23, 25, 26, 27, 28, 28, 29, 17, 22, 23, 25, 26, 27, 28, 28, 29, 13, 15, 16, 
17, 22, 23, 25, 26, 27, 28, 28, 29, 17, 22, 23 ])

#population standar deviation
populationStdDev=5.6

#Point estimate(mean)
sampleSize=
