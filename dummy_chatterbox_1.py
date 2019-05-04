
def azureml_main(dataframe1 = None, dataframe2 = None):
  # Import the nltk module
  import nltk
  
  # Import the pandas package. Pandas package generally used for transform the data.
  import pandas as pd
  
  # Import the Numpy.  fundamental package for scientific computing with Python. use for powerful N-dimensional array object.
  import numpy as np
  
  # Regular expression package
  import re
  
  # Array for token list
  token_list = []
  
  # download the punkt package used for sent_tokenize and word_tokenize
  nltk.download(info_or_id='punkt', download_dir='C:/users/client/nltk_data')
  
  # download the stopword package used for removing the stop words
  nltk.download(info_or_id='stopwords', download_dir='C:/users/client/nltk_data')
  
  # download the wordnet package used for lemmatization
  nltk.download(info_or_id='wordnet',download_dir='C:/users/client/nltk_data')
  
  # Import stopwords
  from nltk.corpus import stopwords
  
  # import WordNetLemmatizer
  from nltk.stem import WordNetLemmatizer
  
  # Get the stopwords for english dictionary
  l_stopwords = stopwords.words('english')
  colnames = dataframe1.columns
  
  # dataframe1 is the one of the input in this package. similar to dataset in .net. get the column of the dataset.
  # get the text from the dataset of the first column in the dataset.
  texts = dataframe1[colnames[0]]
  for index,row in dataframe1.iterrows(): # loop through each row in data set
    corpus = row['text']  # get the text of the first row
  
  for sentence in nltk.sent_tokenize(corpus): # convert the paragraph of the text into sentences
    for token in nltk.word_tokenize(sentence): # convert the sentences into tokens
      if token.lower() not in l_stopwords :  # check each tokens in stop words
        token_list.append(token.lower())  # if not add this to list
  
  wnl = WordNetLemmatizer() # create a object for wor wordnetlemmatizer
  
  # for each word in in token list , get the lemmatization word. for example, running will return run
  for word in token_list:
    token_list1.append(wnl.lemmatize(word).encode("utf8"))
  
  # transfer the array of list to dataset
  dataframe_output = pd.DataFrame(np.array(token_list1), columns=['tokens']) 
  
  # return dataset. Note in azure python scrip module always accept dataset as input and also output also should be dataset.
  return [dataframe_output]
