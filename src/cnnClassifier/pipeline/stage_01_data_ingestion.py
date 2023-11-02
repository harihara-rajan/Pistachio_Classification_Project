from src.cnnClassifier.config.configuration import ConfigurationManager
from src.cnnClassifier.components.data_ingestion import DataIngestion
from src.cnnClassifier import logger

STAGE_NAME = "Data Ingestion"
class DataIngestionPipeline:
    def __init__(self):
        pass
    def main(self):
        conf_manager = ConfigurationManager()
        DataIngestionConfig = conf_manager.get_data_ingestion_config()
        DI = DataIngestion(DataIngestionConfig)
        DI.download_file()
        DI.extract_zip_file()

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>> {STAGE_NAME} started <<<<<<<<<<")
        obj = DataIngestionPipeline()
        obj.main()
        logger.info(f">>>>>>>>> {STAGE_NAME} completed <<<<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
