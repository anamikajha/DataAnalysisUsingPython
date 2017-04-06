
# coding: utf-8

# # Q4_PART ONE
# - use movies_awards dataset.
# - Filer out only the awards column in the dataset
# - Split this column to get no of nominations, awards wons (under all categories)
# - Generate CSV with all information split in different columns

# In[1]:

import os
import pandas as pd
import numpy as np


# In[24]:

#getting current working directory
b = os.getcwd()

#reading the csv file
# Filetring only 15th column i.e the Awards columns from the data
df = pd.read_csv(b+"/"+"movies_awards.csv", usecols=[15]) 


# In[25]:

#printing the top 5 results from the dataset
df.head()

#df.columns


# In[26]:

#replacing & with . from the dataset
df['Awards']=df['Awards'].str.replace(r'&','.') 

#replacing Another from the data
df['Awards']=df['Awards'].str.replace(r'Another','') 


# In[27]:

#removing NA values from data
df = df.dropna()

df.head()


# In[28]:

#creating an output dataframe  with desired columns
output_df=pd.DataFrame(columns=['Awards','Awards_won','Awards_nominated','Prime_awards_Nominated','Oscar_awards_Nominated','Gloden_Globe_Nominate','BAFTA_Awards_Nominated','Prime_awards_Won','Oscar_awards_Won','Gloden_Globe_Won','BAFTA_Awards_Won'])


# In[29]:

for index, row in df.iterrows():
    
#create empty lists for different criteria
    wins=0
    nominations=0
    Oscar_nominations=0
    Oscar_won=0
    Golden_Globe_won=0
    Golden_Globe_nominations=0
    Primetime_nominations=0
    Primetime_won=0
    BAFTA_nominations=0
    BAFTA_won=0
    
    #checking if the column contains NA values
    if type(row['Awards'])!=float:
        
        #split column based on '.'
        row['Awards']=row['Awards'].split('.')
        
        #iterating through each element that we obtained after split
        for i in range(len(row['Awards'])-1):
            
            #check if the values contains 'win'
            if 'win' in row['Awards'][i]:
                #add it to the wins list
                wins+=int(row['Awards'][i].split()[0])
                
            #check if the values contains 'nomination'    
            if 'nomination' in row['Awards'][i]:
                nominations+=int(row['Awards'][i].split()[0])
            
            #check if the values contains 'Oscar'
            if 'Oscar' in row['Awards'][i]:
                
                #check if it contains nominated or won
                if 'Nominated' in row['Awards'][i]:
                    Oscar_nominations+=int(row['Awards'][i].split()[2])
                    nominations+=Oscar_nominations
                if 'Won' in row['Awards'][i]:
                    Oscar_won+=int(row['Awards'][i].split()[1])
                    wins+=Oscar_won
            
            #check if the values contains 'Golden Globe'
            if 'Golden Globe' in row['Awards'][i]:
                
                #check if it contains nominated or won
                if 'Nominated' in row['Awards'][i]:
                    Golden_Globe_nominations+=int(row['Awards'][i].split()[2])
                    nominations+=Golden_Globe_nominations
                if 'Won' in row['Awards'][i]:
                    Golden_Globe_won+=int(row['Awards'][i].split()[1])
                    wins+=Golden_Globe_won
            
            #check if the values contains 'Primetime'
            if 'Primetime Emmy' in row['Awards'][i]:
                
                #check if it contains nominated or won
                if 'Nominated' in row['Awards'][i]:
                    Primetime_nominations+=int(row['Awards'][i].split()[2])
                    nominations+=Primetime_nominations
                if 'Won' in row['Awards'][i]:
                    Primetime_won+=int(row['Awards'][i].split()[1])
                    wins+=Primetime_won
            
            #check if the values contains 'BAFTA'
            if 'BAFTA' in row['Awards'][i]:
                
                #check if it contains nominated or won
                if 'Nominated' in row['Awards'][i]:
                    BAFTA_nominations+=int(row['Awards'][i].split()[2])
                    nominations+=BAFTA_nominations
                if 'Won' in row['Awards'][i]:
                    BAFTA_won+=int(row['Awards'][i].split()[1])
                    wins+=BAFTA_won
        
        #append all the list to output dataframe
        output_df=output_df.append(pd.Series([row['Awards'],wins,nominations,Primetime_nominations,Oscar_nominations,Golden_Globe_nominations,BAFTA_nominations,Primetime_won,Oscar_won,Golden_Globe_won,BAFTA_won],index=['Awards','Awards_won','Awards_nominated','Prime_awards_Nominated','Oscar_awards_Nominated','Gloden_Globe_Nominate','BAFTA_Awards_Nominated','Prime_awards_Won','Oscar_awards_Won','Gloden_Globe_Won','BAFTA_Awards_Won']),ignore_index=True)


#printing top 5 results of the output dataset
output_df.head()


# ## Printing the result in a csv

# In[30]:

#function to check is directory exists
def funCheckDir(path):
    directory = os.path.dirname(path) # defining directory path
    if not os.path.exists(directory): # checking if directory already exists
        os.makedirs(directory) # making a directory


#printing the second csv with total compensation data
resultsPath = b+"/Q3_Part_1.csv"

funCheckDir(resultsPath)

# Saving our result dataFrame to csv file.
output_df.to_csv(resultsPath, index=False, encoding='utf-8')


# ## Converting the .ipynb file to .py file

# In[ ]:



