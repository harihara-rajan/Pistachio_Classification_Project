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