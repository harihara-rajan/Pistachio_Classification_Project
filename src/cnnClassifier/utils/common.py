# functions/snippets that we will be using frequently are defined 
# inside the utils folder.

import os 
# from Box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger
import json
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64
import joblib

@ensure_annotations
def read_yaml(path_to_yaml:Path) -> ConfigBox:
    """Read a yaml file and return a ConfigBox object
    Args:
        path_to_yaml (Path): Path like input
    
    Raises:
        ValueError: If the file is empty or
        e : empty file 
    
    Returns:
    
        ConfigBox: A ConfigBox type
    
    """
    # try:
    with open(path_to_yaml) as yaml_file:
        content = yaml.safe_load(yaml_file)
        logger.info(f"yaml file: {path_to_yaml} loaded successfully")
        return ConfigBox(content)
    # except BoxValueError:
    #     raise ValueError(f"{path_to_yaml} is empty or empty file")
    # except Exception as e:
    #     raise e

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")


@ensure_annotations
def save_json(path_to_json:Path, data: dict) -> None:
    """
    Args:
    
        path_to_json (Path): Path like input
    
        data (dict): Data to be saved in json file
    """
    with open(path_to_json, 'w') as outfile:
        json.dump(data, outfile, indent=4)
        logger.info(f"Saved {path_to_json} successfully")

@ensure_annotations
def load_json(path_to_json:Path) -> ConfigBox:   
    """
    Args:
    
        path_to_json (Path): Path like input
    
    Returns:
    
        ConfigBox: Data in json file
    """
    with open(path_to_json) as json_file: 
        data = json.load(json_file)
        logger.info(f"Loaded {path_to_json} successfully")
    
    return ConfigBox(data)

@ensure_annotations
def save_bins(data:Any, path_to_bin:Path) -> None:
    """ 
    save binary files
    Args:   
        data (Any): Data to be saved in binary file
        path_to_bin (Path): Path to binary file
    """
    joblib.dump(value=data, filename= path_to_bin)
    logger.info(f"Saved binary file to {path_to_bin} successfully")

@ensure_annotations
def load_bins(bin_file:Path) -> Any:
    """ 
    load binary files
    Args:
    
        path_to_bin (Path): Path to binary file
    """
    data = joblib.load(bin_file)
    logger.info(f"Loaded binary file from {bin_file} successfully")
    return data

def decode_image(image_string, file_name):
    imgdata = base64.b64decode(image_string)
    with open(file_name, 'wb') as f:
        f.write(imgdata)
        f.close()

def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())