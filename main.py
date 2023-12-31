from src.cnnClassifier.__init__ import logger

from src.cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from src.cnnClassifier.pipeline.stage_02_base_model import BaseModelPipeline
from src.cnnClassifier.pipeline.stage_03_callbacks import CallbacksPipeline


STAGE_NAME01 = "Data Ingestion"
STAGE_NAME02 = "Base CNN Model"
STAGE_NAME03 = "Callbacks"


try:
    logger.info(f">>>>>>>>> {STAGE_NAME01} started <<<<<<<<<<")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>>> {STAGE_NAME01} completed <<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e
    
try:
    logger.info(f">>>>>>>>> {STAGE_NAME02} started <<<<<<<<<<")
    data_ingestion = BaseModelPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>>> {STAGE_NAME02} completed <<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

try:
    logger.info(f">>>>>>>>> {STAGE_NAME03} started <<<<<<<<<<")
    obj = CallbacksPipeline()
    obj.main()
    logger.info(f">>>>>>>>> {STAGE_NAME03} completed <<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e