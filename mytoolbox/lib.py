from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk import word_tokenize
import string

def cleaning(text, language):
    #Lowercase
    text = text.lower()
    #Punctuation removing 
    for punctuation in string.punctuation:
        text = text.replace(punctuation, '')
    #Stop Words
    stop_words = set(stopwords.words(language))
    word_tokens = word_tokenize(text)
    text = [w for w in word_tokens if not w in stop_words]
    #Numbers removing
    text = [word for word in text if not word.isdigit()]
    #Lematizer
    lemmatizer = WordNetLemmatizer()
    text = ' '.join([lemmatizer.lemmatize(word) for word in text])
    return text 
