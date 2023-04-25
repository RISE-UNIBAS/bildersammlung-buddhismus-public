""" main.py

Main app. """

from scripts.client import Client
from scripts.utility import Utility

import os.path

DIR = os.path.dirname(__file__)
PARENT_DIR = os.path.dirname(os.path.dirname(__file__))
ARCHIVE = f"{PARENT_DIR}/archive"
INDEXING = f"{PARENT_DIR}/indexing"


Client.parsed_field2csv(json_export=Utility.load_json(file_path=f"{INDEXING}/workflow/export_master.json"),
                        save_path=f"{INDEXING}/workflow/analysis/dates_inscribed.csv",
                        field="date",
                        inscribed=True)
Client.parsed_field2csv(json_export=Utility.load_json(file_path=f"{INDEXING}/workflow/export_master.json"),
                        save_path=f"{INDEXING}/workflow/analysis/dates.csv",
                        field="date",
                        inscribed=False)
Client.parsed_field2csv(json_export=Utility.load_json(file_path=f"{INDEXING}/workflow/export_master.json"),
                        save_path=f"{INDEXING}/workflow/analysis/locations_inscribed.csv",
                        field="LocationShown",
                        inscribed=True)
Client.parsed_field2csv(json_export=Utility.load_json(file_path=f"{INDEXING}/workflow/export_master.json"),
                        save_path=f"{INDEXING}/workflow/analysis/locations.csv",
                        field="LocationShown",
                        inscribed=False)
Client.parsed_field2csv(json_export=Utility.load_json(file_path=f"{INDEXING}/workflow/export_master.json"),
                        save_path=f"{INDEXING}/workflow/analysis/creators_inscribed.csv",
                        field="creator",
                        inscribed=True)
Client.parsed_field2csv(json_export=Utility.load_json(file_path=f"{INDEXING}/workflow/export_master.json"),
                        save_path=f"{INDEXING}/workflow/analysis/creators.csv",
                        field="creator",
                        inscribed=False)
Client.persons2csv(json_export=Utility.load_json(file_path=f"{INDEXING}/workflow/export_master.json"),
                   save_path=f"{INDEXING}/workflow/analysis/persons_wide.csv")
Client.persons2csv(json_export=Utility.load_json(file_path=f"{INDEXING}/workflow/export_master.json"),
                   save_path=f"{INDEXING}/workflow/analysis/persons_tall.csv",
                   tall=True)
