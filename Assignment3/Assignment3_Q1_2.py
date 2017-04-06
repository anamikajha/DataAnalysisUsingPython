
# coding: utf-8

# # Q1_Part TWO
# - Use vehicle_collision data.
# - For each Borough find the number of vehicles involved in the accident
# - Generate CSV with 5 columns(Borough, One-vehicle, Two-vehicle, Three-Vehicle, More-Vehicle)

# In[1]:

import os
import pandas as pd


# In[2]:

#getting current working directory
b = os.getcwd()

#reading the csv file
df = pd.read_csv(b+"/"+"Data/vehicle_collisions.csv", parse_dates=['DATE'], usecols=[0,1,3,19,20,21,22,23]) #usecols=[0,1,3]) #vehicle_collisions.csv, , delim_whitespace=True, , header=None


# In[3]:

#listing the columns of the dataset
df.columns


# In[4]:

#filtering out data for date starting 2015-01-01
df=df[(df['DATE'] > '2014-12-31')]

#printing first 5 columns of the dataframe
df.head()


# In[5]:

#Filling out the missing values in Borough with Not Listed
df['BOROUGH'] = df.BOROUGH.fillna('Not Listed')


# In[8]:

#creating subsets of given dataframes 
df_location = df[['UNIQUE KEY','BOROUGH']]
df_vehicle = df[['VEHICLE 1 TYPE','VEHICLE 2 TYPE','VEHICLE 3 TYPE','VEHICLE 4 TYPE','VEHICLE 5 TYPE']]

#checking if the values in vehicle columns are Null
df_type = df_vehicle.notnull()

#converting the null values to 0 and 1
df_type = df_type.applymap(lambda x:1 if x else 0)

#concatenating all data frames in one
df_type = pd.concat([df_location, df_type], axis=1)

#printing the top 5 rows of the resultant data frame
df_type.head()


# In[9]:

#sum the values of different types of vehicle group by Borough
result_df = df_type.groupby(df_type['BOROUGH']).sum().reset_index()

#filtering out desired column in the result dataset
result_df = result_df[['BOROUGH', 'VEHICLE 1 TYPE', 'VEHICLE 2 TYPE', 'VEHICLE 3 TYPE', 'VEHICLE 4 TYPE','VEHICLE 5 TYPE']]

result_df.head()


# In[10]:

#creating a list of desired columns
columns = ['BOROUGH', 'One_Vehicle_Involved', 'Two_Vehicle_Involved', 'Three_Vehicle_Involved', 'More_Vehicle_Involved']

#subtracting the value of columns from each other to get the result
finalResult = pd.DataFrame({'BOROUGH' : result_df['BOROUGH'], 'One_Vehicle_Involved' : result_df['VEHICLE 1 TYPE']-result_df['VEHICLE 2 TYPE'], 
                           'Two_Vehicle_Involved' : result_df['VEHICLE 2 TYPE']-result_df['VEHICLE 3 TYPE'], 'Three_Vehicle_Involved' : result_df['VEHICLE 3 TYPE']-result_df['VEHICLE 4 TYPE'],
                           'More_Vehicle_Involved' : result_df['VEHICLE 4 TYPE'] })

#printing the top 5 results
finalResult.head()


# In[ ]:

#df1 = pd.DataFrame(df.iloc[0:10])


# In[ ]:

#for index, row in df1.iterrows():
   # for i in range(0,len(df1)):
        
        #if((type(df1['VEHICLE 1 TYPE'][i]) == str) and (type(df1['VEHICLE 2 TYPE'][i])!= str)): #& type(df1['VEHICLE 3 TYPE'])==float & type(df1['VEHICLE 4 TYPE'])=float):
           # df1['ONE_VEHICLE_INVOLVED'] = 1
    
       # elif((type(df1['VEHICLE 2 TYPE'][i])== str) and (type(df1['VEHICLE 3 TYPE'][i]) !=str)): #& (pd.isnull(df['VEHICLE 4 TYPE'])== True) & (pd.isnull(df['VEHICLE 5 TYPE'])== True)):
           # df1['TWO_VEHICLE_INVOLVED'] = 1
    
        #elif((type(df1['VEHICLE 3 TYPE'][i])== str) and (type(df1['VEHICLE 4 TYPE'][i]) !=str)): #& (pd.isnull(df['VEHICLE 5 TYPE'])== True)):
           # df1['THREE_VEHICLE_INVOLVED'] = 1
    
       # else:
           # df1['MANY_VEHICLE_INVOLVED'] = 1


# ## printing the result in a csv

# In[ ]:



