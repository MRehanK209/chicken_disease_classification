import os
from pathlib import Path
import logging

logging.basicConfig(
    level = logging.INFO,
    format = '[%(asctime)s]: %(message)s'
)

project_name = "CNN Classifier"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/configs/configuration.py",
    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/entities/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "configs/configs.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirement.txt",
    "setup.py",
    "research/trials.ipynb",
    "template/index.html"
 
]

for file_path in list_of_files:
    file_path = Path(file_path)
    filedir, filename = os.path.split(file_path)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating Directory: {filedir}, for the filename {filename}")

    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path,"w") as f:
            pass
            logging.info(f"Creating the empty file: {file_path}")

    else:
        logging.info(f"{filename} is already exist")