import os
from pathlib import Path
import logging

# FORMAT = '%(asctime)s %(message)s'

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')

project_name = "mlProject"

list_of_flies = [
    f"src/{project_name}/__init__.py", #constructor file
    f"src/{project_name}/components/__init__.py"
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/cofiguration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
    "templates/style.css",
    "templates/script.js"
]


for filepath in list_of_flies:
    filepath = Path(filepath)

    dir,file=os.path.split(filepath)

    if dir != "":
        os.makedirs(dir,exist_ok=True)
        logging.info(f"Directory{dir} created for file{file} successfully")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, "w") as f:
            logging.info(f"Creating files: {filepath} successfully")
    else:
        logging.info("Files{file} already exists")
 


