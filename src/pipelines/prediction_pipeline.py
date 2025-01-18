import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object

class predictPipeline:
    def __init__(self):
        pass 

    def predict(self,features):
        model_path=("artifacts\model.pkl")
        preprocessor_path =("artifacts\preprocessor.pkl")
        model=load_object(file_path=model_path)
        preprocessor=load_object(file_path=preprocessor_path)
        preproceess= preprocessor.transform(features)
        pred=model.predict(preproceess)
        return pred
    
class Custom_data:
    def __init__(self,carat,cut,color,clarity,depth,table,x,y,z):
        self.carat = carat
        self.cut = cut
        self.color = color
        self.clarity = clarity
        self.depth = depth
        self.table = table
        self.x = x
        self.y = y
        self.z = z
    def get_data_as_df(self):
        try:
            data = {
                "carat": [self.carat],
                "cut": [self.cut],
                "color": [self.color],
                "clarity": [self.clarity],
                "depth": [self.depth],
                "table": [self.table],
                "x": [self.x],
                "y": [self.y],
                "z": [self.z]
            }
            return pd.DataFrame(data)
        except Exception as e:
            raise CustomException(e, sys)