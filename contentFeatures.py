import string
import nltk

from collections import Counter
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.porter import *

def get_tokens():
    with open('Phishing_Content.txt', 'r') as shakes: #load text file
        text = shakes.read()
        lowers = text.lower()
        tokenizer = RegexpTokenizer(r'\w\D\w+')  #remove digit and punctuation
        tokens = tokenizer.tokenize(lowers)  #convert all the letters into lowercase
        return tokens

tokens = get_tokens()
count = Counter(tokens)

filtered = [w for w in tokens if not w in stopwords.words('english')] #remove all the stopwords such as 'the', 'in', 'at' etc.
count = Counter(filtered)
print (count.most_common(50))

#stemming: to remove derived words
def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed

stemmer = PorterStemmer()
stemmed = stem_tokens(filtered, stemmer)
count = Counter(stemmed)
print (count.most_common(50)) 
