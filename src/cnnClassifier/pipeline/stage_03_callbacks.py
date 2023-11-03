from src.cnnClassifier.config.configuration import ConfigurationManager
from src.cnnClassifier.components.prepare_callbacks import PrepareCallbacks
from src.cnnClassifier import logger
STAGE_NAME="Prepare Callbacks"
class CallbacksPipeline:
    def __init__(self):
        pass

    def main(self):
        conf_manager = ConfigurationManager()
        prepare_callbacks = conf_manager.prepare_callbacks()
        callbacks = PrepareCallbacks(prepare_callbacks)
        callbacks_cp = callbacks.model_checkpoint_callbacks
        callbacks_es = callbacks.early_stopping_callbacks
        callbacks_tb = callbacks.early_stopping_callbacks

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>> {STAGE_NAME} started <<<<<<<<<<")
        obj = CallbacksPipeline()
        obj.main()
        logger.info(f">>>>>>>>> {STAGE_NAME} completed <<<<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e