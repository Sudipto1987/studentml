import os
import sys
from student_predictor.exception import CustomException
from student_predictor.logger import logging
import pandas as pd
import sklearn

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from student_predictor.components.data_transformation import DataTransformation
from student_predictor.components.data_transformation import DataTransformationConfig

from student_predictor.components.model_trainer import ModelTrainerConfig
from student_predictor.components.model_trainer import ModelTrainer

@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artefacts',"train.csv")
    test_data_path: str=os.path.join('artefacts',"test.csv")
    raw_data_path: str=os.path.join('artefacts',"data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        print(sklearn.__version__)
        # Get the directory where this script is located
        current_dir = os.path.dirname(os.path.abspath(__file__))
        logging.info(f'current directory is {current_dir}')

        # Move up to the root folder and then into notebooks/data
        # .. goes up one level
        data_path = os.path.join(current_dir, '..', '..', '..', 'input', 'data.csv')

        try:
            df=pd.read_csv(data_path)
            logging.info('Read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info("Train test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Ingestion of the data is completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()

    data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)

    modeltrainer=ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr,test_arr))



