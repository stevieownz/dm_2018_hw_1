import string
from nltk.corpus import stopwords
def text_process(text):
   
    #Takes in a string of text, then performs the following:
    #1. Remove all punctuation
    #2. Remove all stopwords
    #3. Return the cleaned text as a list of words
    
    nopunc = [char for char in text if char not in string.punctuation]
    nopunc = ''.join(nopunc)
    
    return [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]