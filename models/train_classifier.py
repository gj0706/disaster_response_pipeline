import sys
import pandas as pd
import numpy as np
import matplotlib as plt
from sqlalchemy import create_engine
import re
import nltk
nltk.download(['punkt','stopwords','wordnet', 'averaged_perceptron_tagger'])
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.model_selection import GridSearchCV
from sklearn.multioutput import MultiOutputClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
import pickle

def load_data(database_filepath):
    """[summary]
    
    Arguments:
        database_filepath {[type]} -- [description]
    Returns:

    """
    engine = create_engine('sqlite:///' + database_filepath)
    df = pd.read_sql('SELECT * FROM Disaster_data', engine)
    X = df['message']    
    y = df.iloc[:,4:]
    return X, y

def tokenize(text):
    """[summary]
    
    Arguments:
        text {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    """
    # Normalize
    text = re.sub(r'[^a-zA-Z0-9]', ' ', text.lower())
    # Tokenization
    words = word_tokenize(text)
    # Remove stop words
    words = [w for w in words if w not in stopwords.words('english')]
    # Lemmatize
    lemmatizer = [WordNetLemmatizer().lemmatize(w) for w in words]
    return lemmatizer


def build_model():
    pass


def evaluate_model(model, X_test, Y_test, category_names):
    pass


def save_model(model, model_filepath):
    pass


def main():
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))
        X, Y, category_names = load_data(database_filepath)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
        
        print('Building model...')
        model = build_model()
        
        print('Training model...')
        model.fit(X_train, Y_train)
        
        print('Evaluating model...')
        evaluate_model(model, X_test, Y_test, category_names)

        print('Saving model...\n    MODEL: {}'.format(model_filepath))
        save_model(model, model_filepath)

        print('Trained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database '\
              'as the first argument and the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/DisasterResponse.db classifier.pkl')


if __name__ == '__main__':
    main()