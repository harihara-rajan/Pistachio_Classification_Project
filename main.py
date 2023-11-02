from src.cnnClassifier.__init__ import logger
print("done")
from src.cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionPipeline

STAGE_NAME = "Data Ingestion"

try:
    logger.info(f">>>>>>>>> {STAGE_NAME} started <<<<<<<<<<")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>>> {STAGE_NAME} completed <<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e