""" main.py

Main app. """

from scripts.client import Client
from scripts.utility import Utility

import os.path

DIR = os.path.dirname(__file__)
PARENT_DIR = os.path.dirname(os.path.dirname(__file__))
ARCHIVE = f"{PARENT_DIR}/archive"
INDEXING = f"{PARENT_DIR}/indexing"
ANALYSIS = f"{PARENT_DIR}/indexing/analysis"

Client.add_normalized_names(tropy_file_path="export_master.json",
                            name_csv_path=f"{ANALYSIS}/prefnames.csv")

exit()
Client.fix_namespace(Utility.load_json(file_path=f"{INDEXING}/workflow/export_master.json"),
                     "test.json")
Client.run_analysis(Utility.load_json(file_path=f"{INDEXING}/workflow/export_master.json"),
                    f"{INDEXING}/analysis",
                    "person",
                    "date",
                    "LocationShown",
                    "creator")
