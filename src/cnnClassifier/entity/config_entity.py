from dataclasses import dataclass
from pathlib import Path

# refer config.yaml file, below we are defining a return type
#1. defining entity
@dataclass(frozen=True) # used to create classes that are primarily meant to store data or to return certain type of objects
class DataIngestionConfig:
    root_dir :Path
    source_URL: str
    local_data_file : Path
    unzip_dir:Path

@dataclass(frozen=True)
class BaseModelConfig:
    root_dir :Path 
    base_model_path: Path
    update_base_model_path: Path
    params_image_size: list
    params_learning_rate: float
    params_include_top: bool
    params_weight: str
    params_classes: int

@dataclass(frozen=True)
class PrepareCallbacksConfig:
    root_dir: Path 
    tensorboard_root_log_dir:Path
    checkpoint_model_file_path: Path
    patience: int
    monitor: str 