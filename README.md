# Disaster response pipeline project
This project is a web app that analyzes disaster data by building a machine learning model that classifies disaster messages. The goal is to direct each message to the relief agency that can provide the quickest assistance. This project was created by Udacity in partnership with Figure Eight, and uses real message data from real situations. 

### Table of Contents
1. [Project Description](#desc)
2. [Installation](#installation)
3. [File Description](#files)
4. [Acknowledgements](#licensing)


## Project Description<a name="desc"></a>
There are three components completed for the project:
- ETL Pipeline: loads and cleans the data, then stores it in a SQLite database

- ML Pipeline: loads the data from SQLite database, builds a text processing and machine learning pipeline, trains and tunes the model using GridSearchCV, outputs the results on the text set and exports the final model as a pickle file.

- Flask Web App : uses Pandas to wrangle data on the Flask backend, uses jinjia2 template engine to create HTML templates, uses Plotly for visualization. 

## Installation <a name="installation"></a>

- Clone this repository to your local folder: 

    `git clone https://github.com/gj0706/disaster_response_pipeline.git`

- Run the following commands in the project's root directory( `disaster_response_pipeline`) to set up your database and model.
    - To run ETL pipeline that cleans data and stores in database:

        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/Disaster_response_data.db`

    - To run ML pipeline that trains classifier and saves the model as `model.pkl`:

        `python models/train_classifier.py data/Disaster_esponse_data.db models/model.pkl`


- Go to the `app` folder and run the following command to run your web app:

    `python run.py`

- Open your web browser and enter http://0.0.0.0:3001/, you will see the web page. 



## File Description<a name="files"></a>
Here is the file structure of the project.
```
|____app
| |____run.py
| |____templates
| | |____master.html
| | |____go.html
|____data_preprocess
| |____categories.csv
| |____messages.csv
| |____ETL Pipeline Preparation.ipynb
| |____ML Pipeline Preparation.ipynb
|____data
| |____Disaster_response_data.db
| |____disaster_messages.csv
| |____process_data.py
| |____disaster_categories.csv
|____models
| |____model.pkl
| |____train_classifier.py
|____README.md
```

## AcKnowledgements<a name="licensing"></a>

Thanks Udacity for providing all the project resources.
Thanks Figure Eight for providing the dataset.  

