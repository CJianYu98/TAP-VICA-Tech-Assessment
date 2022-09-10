# TAP-VICA-Tech-Assessment

## Table of contents
1. [Introduction](#introduction)
2. [Task 1](#task_1)
    1. [Requirements](#task_1_requirements)
3. [Task 2](#task_2)
    1. [Requirements](#task_2_requirements)
    2. [Setup](#task_2_setup)

## Introduction <a name="introduction"></a>
This is a tech assessment repository for GovTech VICA Tech Assessment. This repository consists of 2 folders, each for a task given in the tech assessment.

---
## Task 1 <a name="task_1"></a>
Codes for Task 1 can be found [here](https://github.com/CJianYu98/TAP-VICA-Tech-Assessment/tree/main/task_1).

There is only 1 notebook file, which contains data exploratory analysis, data cleaning and prediction model. Answers for the guiding questions can also be found in the notebook.


## Install Requirements <a name="task_1_requirements"></a>
To install the dependencies required for Task 1:
```
cd task_1
pip install -r requirements.txt
```

---
## Task 2 <a name="task_2"></a>
Codes for Task 2 can be found [here](https://github.com/CJianYu98/TAP-VICA-Tech-Assessment/tree/main/task_2). MongoDB in this task is not deployed and has been ran locally. 

There are 4 files for this task:
- .env -> For setting up environment variables
- connect.py -> For connecting to MongoDB database
- utils.py -> Helper functions 
- run.py -> Main file to run and push original data into MongoDB


## Install Requirements <a name="task_2_requirements"></a>
To install the dependencies required for Task 2:
```
cd task_2
pip install -r requirements.txt
```


## Environment Setup <a name="task_2_setup"></a>
You may key in your MongoDB environment variables respectively
```
DB_URL = "your-database-url"
DB_TABLE_NAME = "your-database-name"
DB_COLLECTION = "your-database-collection-name"
```

For example, to run it locally, you can set the environment variables as such:
```
DB_URL = "mongodb://localhost:27017/"
DB_TABLE_NAME = "test-db"
DB_COLLECTION = "insurance"
```