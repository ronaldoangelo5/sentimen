import pandas as pd
import string
import re
import pickle
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
#from django.templatetags.static import static
import os
from django.conf import settings
neigh = pickle.load(open(os.path.join(settings.STATIC_ROOT[0],'new_model(sentimenta-k20).pkl'), "rb"))
vectorizer = pickle.load(open(os.path.join(settings.STATIC_ROOT[0],'new_tfidf(sentimenta-k20).pkl'), "rb"))

def cleansing(data):
    #lower text
    data = data.lower()

    #hapus punctuation
    remove = string.punctuation
    translator = str.maketrans(remove, ' '*len(remove))
    data = data.translate(translator)

    #remove ASCII dan unicode
    data = data.encode('ascii', 'ignore').decode('utf-8')

    #remove newline
    data = data.replace('\n', ' ')

    return data

def preprocess_data(data):
    #cleansing data
    data = cleansing(data)

    #hapus stopwords
    factory = StopWordRemoverFactory()
    stopword = factory.create_stop_word_remover()
    data = stopword.remove(data)

    #stemming
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()
    data = stemmer.stem(data)

    #count vectorizer
    data = vectorizer.transform([data])

    return data

def sentimenAnalisis(data):
    data = preprocess_data(data)
    predict = neigh.predict(data)
    predict_proba = neigh.predict_proba(data)
    return bool(predict[0]),predict_proba
