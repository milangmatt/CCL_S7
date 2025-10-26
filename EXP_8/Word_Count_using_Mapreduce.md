## Experiment 8

#  Word Count using MapReduce

### AIM

Setup Apache spark on your system and implement a simple word count application

### ALGORITHM

1. Start
2. Create a spark configuration to enable parallel data processing
3. Input a text file with the sample text
4. Store the file contents in a variable and convert it to RDD
5. Split the text into words, apply transformations to split the input line into individual words
6. Transform each word into a key-value pair
7. The key represents the word and the value represents one occurance
8. Group all identical words together by keys
9. Sum all the values for each key to obtain the total count of each word 
10. Display each word along with its total count
11. Stop


### RESULT

The output was obtained successfully