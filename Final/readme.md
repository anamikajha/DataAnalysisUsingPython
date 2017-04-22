
# Final Exam Submission: 
## QUORA Question Pairs Dataset. Can you identify duplicate questions?

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

### Acknowledgements
For more information on this dataset, check out Quora's first dataset release page:
<https://data.quora.com/First-Quora-Dataset-Release-Question-Pairs>

### License
This data is subject to Quora's Terms of Service, allowing for non-commercial use. https://www.quora.com/about/tos
