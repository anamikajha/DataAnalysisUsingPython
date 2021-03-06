# Final Exam Submission: 
### `QUORA Question Pairs Dataset`

### Dependency and Installation from sources
- Python 3.5.2
- Word Cloud
  - pip install wordcloud (XCode needs to be installed beforehand for Mac)
- FuzzyWuzzy : For string comparison
  - pip install python-levenshetein
  - pip install fuzzywuzzy
  
### Dataset : Quora Question Pairs dataset
The dataset is based on actual data from Quora. Quora's first public dataset is related to the problem of identifying duplicate questions. Ideally there should be a single question page for each logically distinct question. For example, the queries “How many states India has” and “What are the number of states in India” should not exist separately on Quora. 
 
Having a separate page for different questions being asked makes knowledge-sharing more efficient in many ways: 
- Lesser redundant data
- Knowledge seekers can access all the answers to a question on a single thread
- Writers can reach a larger readership than if that audience was divided amongst several pages.

### Content
There are over 400,000 lines of potential question duplicate pairs. Each line contains IDs for each question in the pair, the full text for each question, and a binary value that indicates whether the line truly contains a duplicate pair.
![alt tag](https://github.com/anamikajha/DataAnalysisUsingPython/blob/master/Final/Analysis/Extra%20Files/Preview%20of%20data.png)

#### `Analysis 1 : Understanding the dataset and plotting term frquency analysis for each question`
First analysis is more about understanding the dataset. Different types of charts have been incorporated in this analysis to have an easy visual understanding of the dataset. Normalised word share count has been calculated to be used in plots. Common words between the questions and term frequency of these question pair sets have also been calculated. These analysis have been discuss further in detail below.

For starters few mathematical calculations on the dataset have been done to get an idea of:
- percentage of duplicate pair of questions
- number of unique questions in the data
- number of questions that appear multiple times
- percentage of questions with question marks
- percentage of questions that has math tags
- percentage of questions that have punctuation marks in them
- percentage of questions that have capitalized first word
- percentage of questions that has numbers in them 

A histogram plot of number of time a question has repeated has been created.

![alt tag](https://github.com/anamikajha/DataAnalysisUsingPython/blob/master/Final/Analysis/Analysis_1_ExtraFiles/Question%20appearance%20count.png)
In the above bar chart we see that most questions only appear a few times, with very few questions appearing several times (and a few questions appearing many times). One question appears more than 60 times, (We consider this is to be an outlier). This is not an ideal case. Ideally all questions should have one count.

Now some feature analysis has been done on the dataset like extracting the length of questions1 and question 2, counting total number of words in the question pair combined and separate and then calculating the overlapping words (i.e, the common words between the 2 questions in a set). Word share values has been normalised to range between 0 and 1. Plots have been made based on this normalised common words between the two questions.

![alt tag](https://github.com/anamikajha/DataAnalysisUsingPython/blob/master/Final/Analysis/Analysis_1_ExtraFiles/violin_chart%20count%20of%20common%20words.png)

The thickness of the violin plot represents the common words between the two questions. Hence for the non duplicate set of questions the thickness of the plot is more towards the lower value whereas for duplicate set of questions depicted in green the thickness goes upwards.

![alt tag](https://github.com/anamikajha/DataAnalysisUsingPython/blob/master/Final/Analysis/Analysis_1_ExtraFiles/scatter%20plot%20of%20character%20lengths.png)

![alt tag](https://github.com/anamikajha/DataAnalysisUsingPython/blob/master/Final/Analysis/Analysis_1_ExtraFiles/Q1%20length%20vs%20Q2%20length.png)
The above plot is a dynamic plot which shows the common word count between the two questions where the red color represents completely duplicate and blue represents totally non duplicate words.

Character count per question            |  Word count per question
:-------------------------:             |:-------------------------:
![](https://github.com/anamikajha/DataAnalysisUsingPython/blob/master/Final/Analysis/Analysis_1_ExtraFiles/character%20count.png)  |  ![](https://github.com/anamikajha/DataAnalysisUsingPython/blob/master/Final/Analysis/Analysis_1_ExtraFiles/word%20count.png)

The above two histogram plot depicts the number of characters and words per questions. As we see most of the questions character length varies between 25-100 which on an approximation should fall under 5-20 words as shown in the second plot.

![alt tag](https://github.com/anamikajha/DataAnalysisUsingPython/blob/master/Final/Analysis/Analysis_1_ExtraFiles/word%20match%20share%20based%20on%20key%20value%20count.png)

Here we can see that this feature is good at separating the duplicate questions from the non-duplicate ones. Interestingly, it seems very good at identifying questions which are definitely different, but is not so great at finding questions which are definitely duplicates.


#### `Analysis 2 : Analyzing the reason behind pairing of questions`
In this analysis we have studied the pairing of questions. Each question is paired with one other questions. As we have seen in other analysis that these question share a lot of words in common then why a particular question is paired with the respective question in question 2 column? This analysis is specific to non duplicate question set. 

The analysis includes:
- Creating a subset of questions with only non duplicate pair of questions
- Use fuzzywuzzy to compare the content of two questions in the same set. This function gives a matching index value between 0-100 which is stored in a new column as matching index in the dataframe.

Now in the result set we see that there are few columns which shows a matching index of 100%. This should not be the case if these questions are non duplicate.Thus we have separated the question pair with 100% matching index and check if one of the 2 questions is a subset of the other. 

##### `Conclusion: `
In our analysis we see that there are 10454 rows of non duplicate questions and they are all subset of the other question in the pair. Hence 100% matching index is justified. 

#### `Analysis 3 : Categorizing the questions`
For this analysis different categories of questions are created (like explaination, Reasoning, Location based, Numeric, categorical, Timeline, Yes/No questions). A list of all the questions was created (Adding both questions from non duplicate set and adding only one question from duplicate set of questions).Then all the questions from the set are matched against each category of questions.
Now considering the fact that one question may contain two or more questions (like Who is Donald Trump and where does he live?) we have considered all questions with a matching index > = 60% and assigned a weight of 1 to them. Summation of the weight gives us a total count of questions belonging to each category.

NOTE: The total sum of count against all categories may exceed the total count of the questions as one question can belong to more than one category.

##### `Conclusion:`

![alt tag](https://github.com/anamikajha/DataAnalysisUsingPython/blob/master/Final/Analysis/Analysis_3_ExtraFiles/categories%20of%20questions.png)

The total count of questions belonging in each category is then saves as an ouput csv file.

#### `Analysis 4 : Count of questions belonging to trending category`
Of all the questions that were asked in 2016 we want to know how many questions were asked based on the trending topics. A list of all the questions were created (Adding both questions from non duplicate set and adding only one question from duplicate set of questions).A new list of all the trending words in 2017 were created. 

The list of questions were matched against the trending word list and the the total count of questions for each trending words were calculated.

##### `Conclusion:`

Word cloud was implemented to check the same results.

![alt tag](https://github.com/anamikajha/DataAnalysisUsingPython/blob/master/Final/Analysis/Analysis_4_ExtraFiles/wordCloud.png)

#### `Analysis 5 : Sentiment analysis of questions`
In this analysis we have first created a list of all the questions taking similar approach that we have done in previous analysis. Now we create two other list of positive and negative sentiments(These are a set of downloaded csv files from internet). Once we have these three list we now split each question word by word and compare each word to the positive and negative lists. 

Once all the words for a question has been compared we check the count of the positive and the negative words. If the count of positive words are greater then the question is classified in the positive category else negative. If they dont fall in either of the category then it is classified as a neutral sentiment question.

##### `Conclusion:`
In our analysis we see that most of the question falls in the neutral category. They usually dont have emotions attached to them.


### Acknowledgements
For more information on this dataset, check out Quora's first dataset release page:
<https://data.quora.com/First-Quora-Dataset-Release-Question-Pairs>

### License
This data is subject to Quora's Terms of Service, allowing for non-commercial use. https://www.quora.com/about/tos
