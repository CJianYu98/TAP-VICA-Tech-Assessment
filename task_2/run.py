import os

import pandas as pd
from dotenv import load_dotenv

from utils import process_data
from connect import db

# Load environment variables
load_dotenv()

# Constant
INSURANCE_COLLECTION = os.getenv("DB_COLLECTION")

# Select MongoDB collection
insurance = db[INSURANCE_COLLECTION]

# Read data file and process data
df = pd.read_csv("../insurance_data.csv", sep=";")
data = []

# Process data from raw data file
df.apply(lambda x: process_data(data, x), axis=1)

# Check if data is processed correctly
assert len(df) == len(data)

# Insert data into collection
insurance.insert_many(data[i] for i in range(len(data)))