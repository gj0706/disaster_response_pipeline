# Disaster response pipeline project
This project builds a web app that analyzes disaster data to build a model for an API that classifies disaster messages.

### Table of Contents
1. [Installation](#installation)
2. [Project Description](#desc)
3. [File Description](#files)
4. [Results](#results)
5. [Acknowledgements](#licensing)




## Installation <a name="installation"></a>
- Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

- Run the following command in the app's directory to run your web app.
    `python run.py`

- Go to http://0.0.0.0:3001/

## Project Description<a name="desc"></a>

## File Description<a name="files"></a>

## Results<a name="results"></a>

## AcKnowledgements<a name="licensing"></a>
