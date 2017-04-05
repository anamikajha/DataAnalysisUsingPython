
# coding: utf-8

# # Q2_Part TWO
# - use employee_compensation dataset.
# - Filter out the result based on only Calendar year data
# - Find average of all types of compensation for each employee
# - List out the employees whose overtime salary is greater than 5% of their salary
# - For each job family calculate Percentage of total benefits based on average total benefits and average total compensation
# - Generate CSV for all the employee records with overtime salary is greater than 5% of their salary
# - Generate CSV with 4 columns(Job family, Total benefits, Total Compensation and percentage of total benefits)

# In[5]:

import os
import pandas as pd
import numpy as np


# In[6]:

#getting current working directory
b = os.getcwd()

#reading the csv file
df = pd.read_csv(b+"/"+"employee_compensation.csv", usecols=[0,1,9,11,12,13,14,15,16,17,18,19,20,21])


# In[7]:

#printing the top 5 records of the data frame
df.head()


# In[8]:

#filtering data for only Calendar year type
Cal_Data = df[df['Year Type'] == "Calendar"]

Cal_Data.head()


# In[9]:

#Calculating the mean of all the different types of salary columns
AvgSal = df.groupby(['Year','Job Family','Job','Employee Identifier']).mean()


# In[19]:

#printing the first 5 records of the resultant dataset
AvgSal.head()


# In[11]:

#resetting the index of the dataset to create a flat index
AvgSal = AvgSal.reset_index()


# In[12]:

#Filtering the records of employees with overtime value more than 5% of Salaries
Ovrtime_ = AvgSal[AvgSal['Overtime'] > 0.05 * AvgSal['Salaries']]

Ovrtime_.head()


# In[28]:

#Filtering out Job Family, Total Benefits and Total Compensation to a new dataframe
JobFamilyAvg = AvgSal[['Job Family', 'Total Benefits', 'Total Compensation']]
JobFamilyAvg = JobFamilyAvg.groupby(['Job Family']).mean()


# In[29]:

#printing out the top 5 Job family data with average Benefits and Compensation
JobFamilyAvg.head()

#JobFamilyAvg.shape


# In[30]:

#calculating the percentage total benefits columns based on Total Benefits and Total Compensation
JobFamilyAvg['Percent_Total_Benefit'] = (JobFamilyAvg['Total Benefits'] / JobFamilyAvg['Total Compensation']) * 100


# In[31]:

JobFamilyAvg.head()


# In[32]:

#reseting the index to make a flat index
JobFamilyAvg = JobFamilyAvg.reset_index()

JobFamilyAvg


# ## Printing the result in a csv

# In[34]:

#function to check is directory exists
def funCheckDir(path):
    directory = os.path.dirname(path) # defining directory path
    if not os.path.exists(directory): # checking if directory already exists
        os.makedirs(directory) # making a directory

#printing the first csv with overtime data        
resultsPath1 = b+"/Q2_Part_2_overtimeData.csv"

#printing the second csv with total compensation data
resultsPath2 = b+"/Q2_Part_2_PercentTotBenefit.csv"

funCheckDir(resultsPath1)
funCheckDir(resultsPath2)

# Saving our result dataFrame to csv file.
Ovrtime_.to_csv(resultsPath1, index=False, encoding='utf-8')
JobFamilyAvg.to_csv(resultsPath2, index=False, encoding='utf-8')


# In[ ]:




# In[ ]:



