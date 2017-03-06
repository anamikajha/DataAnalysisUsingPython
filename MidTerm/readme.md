
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

For our purposes, we only look at **`sent emails`** and ignore the inboxes of all the employees. Through this approach, we can avoid accidentally analysing the spam emails that are among the received emails. Two main methods of analyses were employed, namely, **`topic modelling with Latent Dirichlet Allocation(LDA)`** and **`sentiment analysis`**.

#### Data processing:
- the emails in their raw form contain a lot of information that is unsuitable for topic modelling analysis.
- Hence we filterd out the header information such as the Date, Subject etc.
- **`Latent Dirichlet Allocation`**  was performed on the dataset with the number of topics, k = 4. The following is a list of the top 10 terms for each of the 4 topics. Note that the words have been stemmed to save memory.

| Meeting | Process | Core   | Casual
| --------|:--------| ------:|:-------
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
