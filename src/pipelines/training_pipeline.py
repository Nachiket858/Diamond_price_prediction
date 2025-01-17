
import os
import sys
# Dynamically add the project root to PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from src.logger import logging
from src.exception import CustomException
import pandas as pd
from src.components.data_transformation import DataTransformation

from src.components.data_ingestion import DataIngestion
from src.components.model_tranner import model_trainer

if __name__ == "__main__":
    obj = DataIngestion()
    train_data_path, test_data_path = obj.initiate_data_ingestion()
    # print(train_data_path,test_data_path)

    data_tranformation = DataTransformation()
    train_arr,test_arr,_=data_tranformation.initiate_data_transformation(train_data_path,test_data_path)
    # print(train_arr,test_arr)
    

    model_trainer= model_trainer()
    model_trainer.initiate_model_traning(train_arr,test_arr)