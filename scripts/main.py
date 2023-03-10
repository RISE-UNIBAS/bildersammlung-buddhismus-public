""" main.py

Main app. """

from scripts.client import Client
from scripts.utility import Utility

import os.path

DIR = os.path.dirname(__file__)
PARENT_DIR = os.path.dirname(os.path.dirname(__file__))
ARCHIVE = f"{PARENT_DIR}/archive"

Client.run_transformation(json_export=Utility.load_json(file_path=f"{ARCHIVE}/archivordnung.json"),
                          save_path=f"{DIR}/test_fix_bug.json")
