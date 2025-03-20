##Part A: Measures of central loca�on. Mean, Median, Lower/Upper Quartiles. 
import statistics as st

# group of 21 bicycles is owned by a bike rental service. Here is the list of ages (in months) for the 
#bicycles: Data set: 12, 13, 17, 2, 23, 15, 27, 5, 11, 8, 13, 5, 20, 14, 3, 17, 8, 10, 21, 16, 13
ages=[12,13,17,2,23,15,27,5,11,8,13,5,20,14,3,17,8,10,21,16,13]
### the mean age of the bycycles
mean_value=st.mean(ages)
print(f"the mean age of the bycycles {mean_value}")
###the median age of the bicycles 
median_value=st.median(ages)
print(f"the median age of the bycycles {median_value}")


quantilesDat=st.quantiles(ages,n=4)
print(quantilesDat)
lowerQuartile=quantilesDat[0]
print(f"Lower quartile is {lowerQuartile}")
upperQuartile=quantilesDat[-1]
print(f"Upper quartile is {upperQuartile}")

##add old bicycle , 225 months old 
ages.append(255)

###the mean age of the bicycles updated
mean_valueUpdated=st.mean(ages)
print(f"the mean age updated of the bycycles {mean_valueUpdated}")

###the median age of the bicycles 
median_valueUpdated=st.median(ages)
print(f"the median age updated of the bycycles {median_valueUpdated}")

##Part B: Measures of variability: Range, standard deviation, variance 



populationA=[8,9,10,11,12] 
populationB=[4,7,10,13,16]

meanPopulationA=st.mean(populationA)
meanPopulationB=st.mean(populationB)
print(f"mean population A is: {meanPopulationA}")
print(f"mean population B is: {meanPopulationB}")


import pandas as pd 
import numpy as np

df_exams=pd.read_csv('StudentsPerformance.csv')
# print(df_exams)
#show first  5 rows in a dataframe
df_exams.head()

#show first 10 rows in a dataframe 
df_exams.head(10)

## show last 5 rows in a dataframe
df_exams.tail()

##getting access to the shape  attribute
df_exams.shape

##showing the info  of the dataframe
df_exams.info()

df_exams_new=df_exams[['math score','reading score','writing score']]

df_exams_new.describe()


