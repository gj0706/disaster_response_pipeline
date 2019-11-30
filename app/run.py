import json
import plotly
import pandas as pd

from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

from flask import Flask, Response
from flask import render_template, request, jsonify
from plotly.graph_objs import Bar
from plotly.graph_objs import Scatter

import plotly.graph_objs as go
from plotly.offline import plot
import random
from sklearn.externals import joblib
from sqlalchemy import create_engine


app = Flask(__name__)

def tokenize(text):
    """ A function that cleans and splits a sentence into words
    
    Arguments:
        text {string} -- a string of sentence 
    
    Returns:
        list of strings -- a list of words
    """
    tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()

    clean_tokens = []
    for tok in tokens:
        clean_tok = lemmatizer.lemmatize(tok).lower().strip()
        clean_tokens.append(clean_tok)

    return clean_tokens

# load data
engine = create_engine('sqlite:///../data/Disaster_response_data.db')
df = pd.read_sql_table('Disaster_data', engine)
# print(df)
# data = df.to_json(orient='records')
# print(data)

# chart_data = df.to_dict(orient='records')
# chart_data = json.dumps(chart_data, indent=2)
# data = {'chart_data': chart_data}

# load model
model = joblib.load("../models/model.pkl")


# index webpage displays cool visuals and receives user input text for model
@app.route('/')

@app.route('/index')
def index():

    # print(data)
    
    # extract data needed for visuals
    genre_counts = df.groupby('genre').count()['message']
    genre_names = list(genre_counts.index)

    classes = (df[df.columns[4:]]==1).sum().reset_index().rename(columns={'index': 'class', 0: 'count'})['class']
    class_df = (df[df.columns[4:]]==1).sum().reset_index().rename(columns={'index': 'class', 0: 'count'})
    class_counts = class_df['count'].sort_values(ascending=False)

    words = classes
    word_freq = 50 *((class_counts - class_counts.min() )/ (class_counts.max() - class_counts.min())) + 20
    colors = [plotly.colors.DEFAULT_PLOTLY_COLORS[random.randrange(1, 10)] for i in range(30)]
    # create visuals
    graphs = [
        {
            'data': [
                Bar(
                    x=genre_names,
                    y=genre_counts
                )
            ],

            'layout': {
                'title': 'Distribution of Message Genres',
                'yaxis': {
                    'title': "Count"
                },
                'xaxis': {
                    'title': "Genre"
                }
            }
        },
        {
            'data': [
                Bar(
                    x=classes,
                    y=class_counts
                )
            ],

            'layout': {
                'title': 'Distribution of classified messages',
                'yaxis': {
                    'title': "Count"
                },
                'xaxis': {
                    'title': "classes"
                }
            }
        },
        {
            'data': [
                Scatter(
                    x=[random.random() for i in range(30)],
                    y=[random.random() for i in range(30)],
                    mode='text',
                    text=words,
                    marker={'opacity': 0.3},
                    textfont={'size': word_freq ,
                            'color': colors}
                    )
            ],

            'layout': {
                'title': 'Word frequency of classified messages',
                'yaxis': {
                    'showgrid': False, 'showticklabels': False, 'zeroline': False
                },
                'xaxis': {
                    'showgrid': False, 'showticklabels': False, 'zeroline': False
                }
            }
        }
    ]
    
    # encode plotly graphs in JSON
    ids = ["graph-{}".format(i) for i, _ in enumerate(graphs)]
    graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)
    
    # render web page with plotly graphs
    return render_template('master.html',  ids=ids, graphJSON=graphJSON)

# @app.route('/get_json')
# def get_json():
#     json = df.to_json(orient='records')
#     response = Response(response=json, status=200, mimetype="application/json")
#     return(response)


# web page that handles user query and displays model results
@app.route('/go')
def go():
    # save user input in query
    query = request.args.get('query', '') 

    # use model to predict classification for query
    classification_labels = model.predict([query])[0]
    classification_results = dict(zip(df.columns[4:], classification_labels))

    # This will render the go.html Please see that file. 
    return render_template(
        'go.html',
        query=query,
        classification_result=classification_results
    )


def main():
    app.run(host='0.0.0.0', port=3001, debug=True)


if __name__ == '__main__':
    main()