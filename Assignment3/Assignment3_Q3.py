
# coding: utf-8

# # Q3_PART ONE
# - Use ‘cricket_matches’ data set.
# - Calculate the average score for each team
# - If a team hosts a game and wins the game, their score can be innings_1 runs or innings_2 runs. It is required to check if the host team won the game, check which innings they played in (innings_1 or innings_2), and take the runs scored in that innings. Calculate average score of each team satisfying the above condition.
# - Generate a csv to print output

# In[1]:

import os
import pandas as pd
import numpy as np


# In[2]:

#getting current working directory
b = os.getcwd()

#reading the csv file
# Filetring only desired columns from the data
df = pd.read_csv(b+"/"+"Data/cricket_matches.csv", usecols=[6,8,12,13,17,18]) 


# In[3]:

#printing top 5 results from the dataset
df.head()


# In[4]:

#filtering the data where the home team is the winner
df_winner = df[df['home'] == df['winner']]
df_winner.head()


# In[5]:

# Offsetting the warning
pd.options.mode.chained_assignment = None

#calculating the score of each team based on which inning they played
df_winner['score'] = np.where(df_winner['home'] == df_winner['innings1'], df_winner['innings1_runs'], df_winner['innings2_runs'])
df_winner.head()


# In[6]:

#calculating the average score of each home
total_score = df_winner['score'].groupby(df_winner['home']).mean()
total_score.head()


# In[8]:

#set the index in the result dataframe
df_result = pd.DataFrame({'home' : total_score.index,'score' : total_score })
df_result.head()


# In[9]:

#function to check is directory exists
def funCheckDir(path):
    directory = os.path.dirname(path) # defining directory path
    if not os.path.exists(directory): # checking if directory already exists
        os.makedirs(directory) # making a directory
        
resultsPath = b+"/Q3_Part_1.csv"
funCheckDir(resultsPath)

# Saving our dataFrame to csv file.
df_result.to_csv(resultsPath, index=False, encoding='utf-8')


# In[ ]:



