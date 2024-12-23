from housing.entity.config_entity import DataIngestionConfig
from housing.exception import HousingException
import os,sys
from housing.logger import logging
from housing.entity.artifact_entity import DataIngestionArtifact



class DataIngestion:

    def __init__(self, data_ingestion_config:DataIngestionConfig):
        try:
             logging.info(f"{'>>'*20}Data Ingestion log started.{'<<'*20} ")
             self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise HousingException(e,sys) from e
        

    def initiate_data_ingestion(self) -> DataIngestionArtifact:

        try:
            pass
        except Exception as e:
            raise HousingException(e,sys) from e

