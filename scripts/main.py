""" main.py

Main app. """

from scripts.client import Client
from scripts.utility import Utility

import os.path

DIR = os.path.dirname(__file__)
PARENT_DIR = os.path.dirname(os.path.dirname(__file__))
ARCHIVORDNUNG = f"{PARENT_DIR}/Archivordnung"

Client.run_transformation(json_export=Utility.load_json(file_path=f"{ARCHIVORDNUNG}/archivordnung.json"),
                          save_path=f"{DIR}/test_export_19.json")
