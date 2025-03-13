import statistics as st
import matplotlib.pyplot as plt
raindata=[2,5,4,4,1,2,7,8,8,8,1,3]
print(raindata)

#Find the Mean,Median and the mode of the data
mean=st.mean(raindata)
median=st.median(raindata)
mode=st.mode(raindata)
harmonic_mean=st.harmonic_mean(raindata)
geometric_mean=st.geometric_mean(raindata)

#this is the mean
print(f"Mean={mean}")
#this is the median
print(f"Median={median}")
#this is the mode
print(f"Mode={mode}")
#this is the h_mean
print(f"Harmonic Mean={harmonic_mean}")
#this is the g_mean
print(f"Geometric Mean={geometric_mean}")


plt.axvline(x=mean,c='yellow',label='Mean')
plt.axvline(x=geometric_mean,c='black',label='Geometric Mean')
plt.axvline(x=harmonic_mean,c='green',label='Harmonic mean')
plt.legend()
# plt.show()


##### USE OF Numpy #####

import numpy as np



mean_np=np.mean(raindata)
print(f"Mean by numpy={mean_np}")
median_np=np.median(raindata)
print(f"Median by numpy={median_np}")


##### USE OF SciPy ######

from scipy import stats
from scipy import mean
from scipy.stats import gmean
from scipy.stats import hmean

import warnings
warnings.filterwarnings("ignore")

Arithmetic_mean=mean(raindata)
print(f"Arithmetic mean={Arithmetic_mean}")
Geometric_mean=gmean(raindata)
print(f"Geometric mean={Geometric_mean}")
Harmonic_mean=hmean(raindata)
print(f"Harmonic mean={Harmonic_mean}")

