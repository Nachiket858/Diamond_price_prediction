from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from src.utils import save_object
import sys,os
from dataclasses import dataclass
import pandas as pd
import numpy as np
from src.exception import CustomException
from src.logger import logging

## data Tranformation config
@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join("artifacts",'preprocessor.pkl')

## data tranformation class
class DataTransformation:
    def __init__(self):
        self.data_tranformation_config = DataTransformationConfig()


    def get_data_tranformation_object(self):
        try:
            logging.info("data transformation started")

            cat_col=['cut', 'color', 'clarity']
            num_col=['carat', 'depth', 'table', 'x', 'y', 'z']


            Color_cat= ['D', 'E', 'F', 'G', 'H', 'I', 'J']
            Clarity_cat= ['I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF']
            Cut_cat= ['Fair', 'Good', 'Very Good', 'Premium', 'Ideal']

            logging.info("pipeline Initiated")
            num_pipeline =Pipeline(
                steps=[
                    ('imputer',SimpleImputer(strategy='median')),
                    ('scaler',StandardScaler())
                ]
            )

            cat_pipeline = Pipeline(
                steps=[
                    ('imputer', SimpleImputer(strategy='most_frequent')),
                    ('ordinalencoder',OrdinalEncoder(categories=[Cut_cat,Color_cat,Clarity_cat])),
                    ('Scaler',StandardScaler())
                ]
            )

            preprocessor = ColumnTransformer([
                ('numerical', num_pipeline, num_col),
                ('categorical', cat_pipeline, cat_col)
            ])
            logging.info("pipeline Completed")
            return preprocessor 

        except Exception as e:
            logging.info("error in data transformation")
            raise CustomException(e,sys)

    def initiate_data_transformation(self,train_data_path,test_data_path):
        try:
            # reading train and test data
            train_df= pd.read_csv(train_data_path)
            test_df= pd.read_csv(test_data_path)

            preprocessing_obj = self.get_data_tranformation_object()

            target_column_name = 'price'
            drop_columns =[target_column_name,'id']
                ## dividing dependent and independed
            input_feature_train_df = train_df.drop(columns=drop_columns,axis=1)
            target_feature_train_df = train_df[target_column_name]
    
            input_feature_test_df = test_df.drop(columns=drop_columns,axis=1)
            target_feature_test_df = test_df[target_column_name]

            ## aplying the tranfoemation
            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)
            

            train_arr = np.c_[input_feature_train_arr,np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr,np.array(target_feature_test_df)]

            save_object(file_path=self.data_tranformation_config.preprocessor_obj_file_path,obj=preprocessing_obj)
            logging.info("preprocessor pickel is creadted and save")

            return train_arr, test_arr, self.data_tranformation_config.preprocessor_obj_file_path
        
        except Exception as e:
            logging.info("exception occiue in data transformation")
            raise CustomException(e,sys)

     