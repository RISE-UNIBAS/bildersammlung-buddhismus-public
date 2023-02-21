""" utility.py

Utility class. """

from __future__ import annotations
from typing import List, Dict, Union
from json import load, dump


class Utility:
    """ A collection of utility functions. """

    @staticmethod
    def load_json(file_path: str) -> dict:
        """ Load a JSON object from file.

        :param file_path: complete path to file including filename and extension
        """

        with open(file_path, encoding="utf-8") as file:
            loaded = load(file)

            return loaded

    @staticmethod
    def save_json(data: Union[List, Dict],
                  file_path: str) -> None:
        """ Save data as JSON file.

        :param data: the data to be saved
        :param file_path: complete path to file including filename and extension
        """

        with open(file_path, "w") as file:
            dump(data, file, indent=4)
