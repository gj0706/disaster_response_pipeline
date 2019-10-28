import sys
import numpy as np
import pandas as pd
import matplotlib as plt
from sqlalchemy import create_engine

def load_data(messages_filepath, categories_filepath):
    """ Function to load datasets
    Arguments:
        messages_filepath {string} -- a string of path of file to load
        categories_filepath {string} -- another string of path of file to load
    Returns:
        df{dataframe} -- a dataframe that merged the two files together
    """
    # load messages dataset
    messages = pd.read_csv('messages.csv')
    categories = pd.read_csv('categories.csv')
    df = messages.merge(categories, on='id')
    return df

def clean_data(df):
    """ Function to clean the data
    Arguments:
        df {pandas dataframe} -- a dataframe to clean
    Returens: 
        df {pandas dataframe} -- cleaned df

    """
    # Split categories into separate category columns.
    categories = df['categories'].str.split(';',expand=True) # create a dataframe of the 36 individual category columns
    row = categories.loc[0,:] # select the first row of the categories dataframe
    category_colnames = row.apply(lambda x : x.split('-')[0]) #extract a list of new column names for categories.
    categories.columns = category_colnames # rename the columns of `categories`

    # use one hot encoding to convert category values into 0/1
    for column in categories:
        categories[column] = categories[column].str[-1] # set each value to be the last character of the string
        categories[column] = categories[column].astype(int) # convert column from string to numeric
   
    # Replace categories column in df with new category columns.
    df.drop('categories', axis=1, inplace=True)
    df = pd.concat([df, categories], axis=1)

    # Remove duplicates
    df.drop_duplicates(inplace = True)
    return df

def save_data(df, database_filename):
    """ Save teh clean dataset into a sqlite database
    
    Arguments:
        df {pandas datafram} -- clean dataset
        database_filename {string} -- output filename (with .db)
    Returns:
        Nome
    """
    engine = create_engine('sqlite:///{}'.format(database_filename))
    
    df.to_sql('Disaster_data', engine, index=False)


def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()