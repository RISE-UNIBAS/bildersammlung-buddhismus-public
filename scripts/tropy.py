""" tropy.py

 Tropy class. """

from __future__ import annotations
from scripts.utility import Utility


class Tropy:
    """ A representation of a Tropy export.

    :param json_export: loaded Tropy JSON export file
    """

    def __init__(self,
                 json_export: dict) -> None:
        self.json_export = json_export
        self.graph = self.json_export["@graph"]

    def validate(self) -> None:
        """ Validate items. """

        self.validate_list()
        self.validate_type()
        self.validate_photo()

    def validate_list(self) -> None:
        """ Validate item list. """

        for item in self.graph:
            try:
                if len(item["list"]) > 3:
                    print(f"Warning: Invalid list in item titled '{item['title']}': List is too large!")
            except KeyError:
                print(f"Warning: Invalid list in item titled '{item['title']}': Missing list items or empty list!")

    def validate_type(self) -> None:
        """ Validate item type. """

        types = ["Ordner",
                 "Klarsichtmappe",
                 "Fotoblatt",
                 "Geheftete Blätter",
                 "Blatt",
                 "Aufgeklebt",
                 "Zwischenblatt"]

        for item in self.graph:
            try:
                item["type"] in types
            except KeyError:
                print(f"Warning: Invalid type in item titled '{item['title']}'!")

    def validate_photo(self) -> None:
        """ Validate item photo. """

        for item in self.graph:
            try:
                len(item["photo"]) % 2 == 0
            except KeyError:
                print(f"Warning: Item titled '{item['title']}' is missing at least one photo!")

    def get_image_sizes(self) -> dict:
        """ Return images sizes. """

        sizes = dict()

        for item in self.graph:
            try:
                # items to skip:
                if "Makulatur" in item["list"]:
                    continue
                elif "Dubletten" in item["tag"]:
                    continue
            except KeyError:
                try:
                    for photo in item["photo"]:
                        if "format" in photo.keys():
                            try:
                                sizes[photo["format"]] += 1
                            except KeyError:
                                sizes[photo["format"]] = 1
                except KeyError:
                    continue

        return sizes

    def save(self,
             file_path) -> None:
        """  Save Tropy export to file path.

        :param file_path: complete path to file including filename and extension
        """

        Utility.save_json(data=self.json_export,
                          file_path=file_path)
