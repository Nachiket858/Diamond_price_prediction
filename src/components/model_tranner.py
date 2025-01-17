from sklearn.preprocessing import OrdinalEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import (
    RandomForestRegressor,
    GradientBoostingRegressor,
    AdaBoostRegressor
)
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR

from xgboost import XGBRegressor
from lightgbm import LGBMRegressor
from catboost import CatBoostRegressor
import sys
import os
from dataclasses import dataclass
import pandas as pd
import numpy as np
from src.exception import CustomException
from src.logger import logging
from src.utils import save_object, evaluate_model



@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join('artifacts','model.pkl')

class model_trainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()
    
    def initiate_model_traning(self,train_arr,test_arr):
        try:
            logging.info("spliting the independend and dependent feature")
            X_train,y_train,X_test,y_test=(
                train_arr[:,:-1],
                train_arr[:,-1],
                test_arr[:,:-1],
                test_arr[:,-1]
            )
            
            models = {
                'LinearRegression': LinearRegression(),
                "Lasso": Lasso(),
                'Ridge': Ridge(),
                'ElasticNet': ElasticNet(),
                'DecisionTree': DecisionTreeRegressor(),
                'RandomForest': RandomForestRegressor(),
                
            }
            
            model_report:dict=evaluate_model(X_train,y_train,X_test,y_test,models)
            print("model_report")
            print('\n====================================================================================')
            logging.info(f'model report:{model_report}')

            ## to get best model score 
            best_model_score = max(sorted(model_report.values()))
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            best_model = models[best_model_name] 
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print(f"best model name:{best_model_name}, r2_score :{best_model_score}")
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            
            save_object(file_path=self.model_trainer_config.trained_model_file_path,obj=best_model)
            
            
        except Exception as e:
            logging.info("error during model training")
            raise CustomException(e,sys)