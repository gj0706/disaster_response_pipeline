# Disaster response pipeline project
This project builds a web app that analyzes disaster data to build a model for an API that classifies disaster messages.

### Table of Contents
1. [Installation](#installation)
2. [Project Description](#desc)
3. [File Description](#files)
4. [Acknowledgements](#licensing)




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

## Project Description<a name="desc"></a>

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

