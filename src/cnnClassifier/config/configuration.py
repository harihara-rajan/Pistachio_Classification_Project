from src.cnnClassifier.constants.__init__ import PARAMS_FILE_PATH,CONFIG_FILE_PATH 
from src.cnnClassifier.utils.common import read_yaml, create_directories
from src.cnnClassifier.entity.config_entity import (DataIngestionConfig, BaseModelConfig)
from pathlib import Path

class ConfigurationManager:
    def __init__(
        self, 
        config_file_path = CONFIG_FILE_PATH,
        params_file_path = PARAMS_FILE_PATH):

        self.config= read_yaml(config_file_path) # return ConfigBox object with 'artifacts_root' as a key name
        self.params= read_yaml(params_file_path)
        create_directories([self.config.artifacts_root])


    def get_data_ingestion_config(self) -> DataIngestionConfig: # see two cells above for DataIngestionConfig 
        config = self.config.data_ingestion
        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
        return data_ingestion_config
    
    def get_base_model_config(self)-> BaseModelConfig: 
        config = self.config.prepare_base_model
        base_model_config = BaseModelConfig(
            root_dir = Path(config.root_dir),
            base_model_path = Path(config.base_model_path),
            update_base_model_path = Path(config.update_base_model_path),
            params_image_size = self.params.IMAGE_SIZE,
            params_learning_rate= self.params.LEARNING_RATE,
            params_include_top = self.params.INCLUDE_TOP,
            params_weight = self.params.WEIGHTS,
            params_classes = self.params.CLASSES
        )
        return base_model_config