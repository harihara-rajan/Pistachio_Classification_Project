from src.cnnClassifier.config.configuration import ConfigurationManager
from src.cnnClassifier.components.base_model import BaseModel
from src.cnnClassifier import logger


STAGE_NAME = "Base Model"

class BaseModelPipeline:
    def __init__(self):
        pass
    def main(self):
        conf_manager = ConfigurationManager()
        BaseModelConfig = conf_manager.get_base_model_config()
        vggmodel = BaseModel(BaseModelConfig)
        vggmodel.get_base_model()
        vggmodel.update_base_model()

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>> {STAGE_NAME} started <<<<<<<<<<")
        obj = BaseModelPipeline()
        obj.main()
        logger.info(f">>>>>>>>> {STAGE_NAME} completed <<<<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e