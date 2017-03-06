
# Midterm Submission
### Dependency and Installation from sources
- Python 3.5.2
- NY Times Article
  - pip install nytimesarticle
- Matplotlib
  - pip install matplotlib
- Store API key as environment variable

## Question 1 : Exploratory Data Analysis of Enron Emails
### Dataset : CMU ENRON Dataset
`1.82 GB of email data from all the employees of ENRON starting from December 1999 to November 2001`

![alt tag](https://image.slidesharecdn.com/exploringtheenronemaildatasetwithkijiandhive-130913140714-phpapp01/95/exploring-the-enron-email-dataset-with-kiji-and-hive-8-638.jpg?cb=1403027558)

- This dataset contains data from about 150 users, mostly senior management of Enron, organized into folders. 
- The corpus contains a total of about 0.5 million messages.

The dataset consists of 517,431 messages that belong to 150 users, mostly senior management of the Enron Corp. Although the
dataset is huge, folders of particular users are often quite sparse.

For our purposes, we only look at **`sent emails`** and ignore the inboxes of all the employees. Through this approach, we can avoid accidentally analysing the spam emails that are among the received emails. Two main methods of analyses were employed, namely, topic modelling with **`Latent Dirichlet Allocation(LDA)`** and **`sentiment analysis`**.

#### Data processing:
- the emails in their raw form contain a lot of information that is unsuitable for topic modelling analysis.
- Hence we filterd out the header information such as the Date, Subject etc.
- **`Latent Dirichlet Allocation`**  was performed on the dataset with the number of topics, k = 4. The following is a list of the top 10 terms for each of the 4 topics. Note that the words have been stemmed to save memory.

| Meeting | Process | Core   | Casual
| --------|:--------|:-------|:-------
| message | enron   | market | thank
| origin  | deal    | gas    | call
| pleas   |agreement| price  | time
| email   | chang   | power  | meet
| thank   | corp    | cpmpani| look
| attach  | fax     | energi | week
| file    | houston | trade  | day
| copi    | contract| busi   | dont
| inform  | date    | servic | vinc
| receiv  | america | manag  | talk


1. Topic 1 contains a lot of meeting related words, perhaps they are from emails that were sent as meeting notices.
2. Topic 2 while related to business seems to be more about the process rather than the content of the core business. It has a lot of terms relevant to business legalities.
3. Topic 3 contains words that are directly related to the core business of Enron like ”gas”, ”power” etc.
4. Topic 4 also seems to be meeting-related but in a more casual tone and setting.

## Analysis:

![alt tag] (https://github.com/anamikajha/DataAnalysisUsingPython/blob/master/MidTerm/Extra%20Files/Monthly%20count%20of%20words.png)

Clearly, there is an abnormal spike in the word counts in the month of March when Jefferey Skiing was replaces by Kenneth Lay as CEO in 2001. This could have resulted in a lot of mail chains between the top officials in the organisation. As we see the maximum pike is for process word counts which could be because of the change in process with new CEO. The trend then gradually declines followed by a steady increase near August. The abnormal spike can be explained Enron’s exemplary
performance, Fortune Magazine had just named Enron as the ”Most Innovative American Company” 3 times in a row and the stock
price of Enron was at an all-time high.  

We again see a dip in the word counts of process words in October, this is when 
- Enron reported a $618 million loss and $1.2 billion value right off. 
- Enrons stock price dropped to alomst half of its price in this month

Casual vs Process count            |  Message vs Core count
:-------------------------:        |:-------------------------:
![](https://github.com/anamikajha/DataAnalysisUsingPython/blob/master/MidTerm/Extra%20Files/casual%20count%20vs%20Process%20count.png)  |  ![](https://github.com/anamikajha/DataAnalysisUsingPython/blob/master/MidTerm/Extra%20Files/Message%20count%20vs%20core%20count.png)

## Conclusion:
In conclusion, although topic modelling and sentiment analysis do provide some useful insights into the data, it is still unclear as to whether they can be used as investigation tools. However, with that being said, there are
some ways in which the analysis can be improved upon. For example, analysis can be conducted by focusing on users who directories are especially large, namely, Sally Beck (Chief Operating Officer), Darren Farmer (Logistics Manager), Vincent Kaminski (Head of Quantitative Modeling Group), Louise Kitchen (President of EnronOnline), Michelle Lokay (Administrative
Assistant), Richard Sanders (Assistant General Counsel) and Williams III (Senior Analyst). This would ensure that only the emails of most relevant people to the scandal are examined and this might reveal more interesting patterns.

## References:
- https://www.stat.berkeley.edu/~aldous/Research/Ugrad/HarishKumarReport.pdf
- http://www.investopedia.com/updates/enron-scandal-summary/
