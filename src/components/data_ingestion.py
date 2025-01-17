import os
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

# Start the data ingestion 
@dataclass
class DataIngestionConfig:
    """This class contains configuration related to data ingestion."""
    train_data_path = os.path.join("artifacts", 'train.csv')
    test_data_path = os.path.join("artifacts", 'test.csv')
    raw_data_path = os.path.join("artifacts", 'raw.csv')


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Data ingestion method started")
        try:
            # Read the data from the file
            df = pd.read_csv(os.path.join("notebooks/data", 'gemstone.csv'))
            logging.info("Dataset read as Pandas DataFrame")

            # Create directory for saving artifacts if it doesn't exist
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)

            # Save raw data
            df.to_csv(self.ingestion_config.raw_data_path, index=False)
            logging.info("Raw data saved")

            # Train-test split
            logging.info("Train-test split initiated")
            train_set, test_set = train_test_split(df, test_size=0.30, random_state=42)

            # Save train and test data
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            logging.info("Data ingestion completed")

            return self.ingestion_config.train_data_path, self.ingestion_config.test_data_path

        except Exception as e:
            logging.error("Error occurred in data ingestion")
            raise CustomException(e, sys)
