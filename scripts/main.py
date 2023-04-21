""" main.py

Main app. """

from scripts.client import Client
from scripts.utility import Utility

import os.path

DIR = os.path.dirname(__file__)
PARENT_DIR = os.path.dirname(os.path.dirname(__file__))
ARCHIVE = f"{PARENT_DIR}/archive"
INDEXING = f"{PARENT_DIR}/indexing"

Client.persons2csv(json_export=Utility.load_json(file_path=f"{INDEXING}/workflow/export_master.json"),
                   save_path=f"{INDEXING}/workflow/persons_wide.csv")
Client.persons2csv(json_export=Utility.load_json(file_path=f"{INDEXING}/workflow/export_master.json"),
                   save_path=f"{INDEXING}/workflow/persons_tall.csv",
                   tall=True)