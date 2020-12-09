import string
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

"""
Check punkt
"""
try:
    nltk.data.find('tokenizers/punkt')
except:
    nltk.download('punkt')

"""
Check wordnet
"""
try:
    nltk.data.find('corpora/wordnet')
except:
    nltk.download('wordnet')

"""
Check stopwords
"""
try:
    nltk.data.find('corpora/stopwords')
except:
    nltk.download('stopwords')


stop_words = set(stopwords.words('english'))
lemma = WordNetLemmatizer()


def remove_urls(text):
    new_text = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", text).split())
    return new_text


# make all text lowercase
def text_lowercase(text):
    return text.lower()  # remove numbers


def remove_numbers(text):
    result = re.sub(r'\d+', '', text)
    return result  # remove punctuation


def remove_punctuation(text):
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)  # tokenize


def tokenize(text):
    text = word_tokenize(text)
    return text  # remove stopwords


def remove_stopwords(text):
    text = [i for i in text if not i in stop_words]
    return text  # lemmatize


def lemmatize(text):
    text = [lemma.lemmatize(token) for token in text]
    return text


def textPreProcess(text):
    text = text_lowercase(text)
    text = remove_urls(text)
    text = remove_numbers(text)
    text = remove_punctuation(text)
    text = tokenize(text)
    text = remove_stopwords(text)
    text = lemmatize(text)
    text = ' '.join(text)
    return text
