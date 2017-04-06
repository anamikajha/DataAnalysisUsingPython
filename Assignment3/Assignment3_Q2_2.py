
# coding: utf-8

# # Q2_Part TWO
# - use employee_compensation dataset.
# - Filter out the result based on only Calendar year data
# - Find average of all types of compensation for each employee
# - List out the employees whose overtime salary is greater than 5% of their salary
# - For each job family calculate Percentage of total benefits based on average total benefits and average total compensation
# - Generate CSV for all the employee records with overtime salary is greater than 5% of their salary
# - Generate CSV with 4 columns(Job family, Total benefits, Total Compensation and percentage of total benefits)

# In[1]:

import os
import pandas as pd
import numpy as np


# In[2]:

#getting current working directory
b = os.getcwd()

#reading the csv file
df = pd.read_csv(b+"/"+"Data/employee_compensation.csv", usecols=[0,1,9,11,12,13,14,15,16,17,18,19,20,21])


# In[3]:

#printing the top 5 records of the data frame
df.head()


# In[4]:

#filtering data for only Calendar year type
Cal_Data = df[df['Year Type'] == "Calendar"]

Cal_Data.head()


# In[5]:

#Calculating the mean of all the different types of salary columns
AvgSal = df.groupby(['Year','Job Family','Job','Employee Identifier']).mean()


# In[6]:

#printing the first 5 records of the resultant dataset
AvgSal.head()


# In[7]:

#resetting the index of the dataset to create a flat index
AvgSal = AvgSal.reset_index()


# In[8]:

#Filtering the records of employees with overtime value more than 5% of Salaries
Ovrtime_ = AvgSal[AvgSal['Overtime'] > 0.05 * AvgSal['Salaries']]

Ovrtime_.head()


# In[9]:

#Filtering out Job Family, Total Benefits and Total Compensation for employees with overtime > 5% of salary to a new dataframe
JobFamilyAvg = Ovrtime_[['Job Family', 'Total Benefits', 'Total Compensation']]
JobFamilyAvg = JobFamilyAvg.groupby(['Job Family']).mean()


# In[10]:

#printing out the top 5 Job family data with average Benefits and Compensation
JobFamilyAvg.head()

#JobFamilyAvg.shape


# In[11]:

#calculating the percentage total benefits columns based on Total Benefits and Total Compensation
JobFamilyAvg['Percent_Total_Benefit'] = (JobFamilyAvg['Total Benefits'] / JobFamilyAvg['Total Compensation']) * 100


# In[12]:

JobFamilyAvg.head()


# In[14]:

#reseting the index to make a flat index
JobFamilyAvg = JobFamilyAvg.reset_index()

#sorting with highest values first
JobFamilyAvg = JobFamilyAvg.sort_values(['Percent_Total_Benefit'], ascending=[False])

#printing the top 5 percent total benefits
JobFamilyAvg.head()


# ## Printing the result in a csv

# In[15]:

#function to check is directory exists
def funCheckDir(path):
    directory = os.path.dirname(path) # defining directory path
    if not os.path.exists(directory): # checking if directory already exists
        os.makedirs(directory) # making a directory

#printing the result data        
resultsPath = b+"/Q2_Part_2.csv"

funCheckDir(resultsPath)

# Saving our result dataFrame to csv file.
JobFamilyAvg.to_csv(resultsPath, index=False, encoding='utf-8')


# ## Converting the .ipynb file to .py file

# In[16]:

get_ipython().system('jupyter nbconvert --to script Assignment3_Q2_2.ipynb')


# In[ ]:



