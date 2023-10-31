"""
author - Hari (M.Sc Computational Science)
"""

import os 
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:') # preferred logging
"""
we are logging only information level log 
first it gets the asci time along with the logging message
"""

project_name = "cnnClassifier"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
] # specify the list of files that you need to create 

for filepath in list_of_files:
    # windows use backward slash instead of forward
    filepath = Path(filepath) # -> convert linux type pathto windows type path
    filedir, filename = os.path.split(filepath)

    if filedir !="": # if filedir is not empty
        os.makedirs(filedir, exist_ok=True) # true -> creates only one time 
        logging.info(f"Creating directroy; {filedir} for the file {filename}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        """
        first checking if the file exists or not and if it is not, it gets into the loop
        """
        with open(filepath, "w") as f:
            pass
            logging.info(f"creating empty file : {filepath}")

    else: # there is already existing file 
        logging.info(f"{filename} already exists")

"""
.gitkeep -> used to keep track of empty folders as well 

Purpose of __init__.py: The __init__.py file serves a few purposes:

1. It signifies that the folder it's in is a Python package.

2. Local Package Concept: When you're working on a Python project and 
you have a directory (folder) that you want to use as a package, 
you create an __init__.py file inside that directory. This file could be 
blank or it could have some Python code that you want to execute when the package is imported.

3. For example, imagine you have a directory called my_package, and it contains multiple Python 
files. To tell Python that my_package is a package, you'd add an empty __init__.py file inside 
the my_package directory. This way, you can use my_package in your Python code as a package and 
import modules from it.

research/trials.ipynb -. to conduct experiements before deployment
"""