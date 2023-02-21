""" items.py

Item classes. """

from __future__ import annotations
from dataclasses import dataclass, asdict
from scripts.metadata import Metadata
from typing import List, Dict


@dataclass
class Item:
    """ A representation of a Tropy item. """

    template: str = "https://tropy.org/v1/templates/id#iTbU0YBP"
    title: str = None
    creator: str = None
    date: str = None
    type: str = None
    source: str = None
    collection: str = None
    box: str = None
    folder: str = None
    object: str = None
    identifier: str = None
    rights: str = None
    hasPart: str = None
    isPartOf: str = None
    isRelatedTo: str = None
    list: List[str] = None
    photo: List[Dict] = None
    tag: list = None

    def list2metadata(self) -> None:
        """ Map (validated) list content to metadata fields. """

        try:
            if "Makulatur" in self.list:
                return None
            else:
                self.box = self.list[0]
                self.folder = self.list[1]
                self.object = self.list[2]
        except (IndexError, TypeError):
            print(f"Warning: Invalid list in item titled '{self.title}': Missing list items or empty list!")

    def serialize(self) -> dict:
        """ Serialize item as dictionary. """

        serialized = {"@item": "item"}
        serialized.update(asdict(self))

        return serialized

    def transform(self,
                  item: Item,
                  photo: dict,
                  identifier: str) -> None:
        """ Transform item. """

        # restructure metadata:
        self.copy_metadata_from_item(item, "type")
        self.photo = [photo]

        # assign ID (only assigned to item not to recto/verso view):
        self.identifier = identifier

        # assign signature:
        self.make_signature()

        # assign title:
        self.make_title()

    def copy_metadata_from_dict(self, dictionary: dict) -> None:
        """ Copy metadata from dictionary. """

        try:
            for key in dictionary.keys():
                self.__setattr__(key, dictionary[key])
        except Exception:
            raise

    def copy_metadata_from_item(self,
                                item: Item,
                                *args):
        """ Copy metadata from item.

        :param item: the item from which metadata is copied
        :param args: deselected attributes (values not copied)
        """

        for key in item.serialize().keys():
            try:
                if key in args:
                    continue
                else:
                    self.__setattr__(key, item.serialize()[key])
            except Exception:
                raise

    def make_signature(self) -> None:
        """ Write to self.source signature. """

        self.source = f"{self.box}-{self.folder}-{self.object}-{self.identifier}"

    def make_title(self) -> None:
        """ Write to self.title title. """

        self.title = f"{Metadata.get_folder_mapping()[self.box]} - {self.identifier}"

    @classmethod
    def get_str_mapping(cls):
        """ Get mapping from item string name to class. """

        return {"Fotoblatt": Fotoblatt,
                "Foto": Foto,
                "Blatt": Blatt,
                "Aufgeklebt": Aufgeklebt}


@dataclass
class Fotoblatt(Item):
    """ A representation of a Tropy item with the 'Fotoblatt' type. """

    type: str = "Fotoblatt"


@dataclass
class Foto(Item):
    """ A representation of a Tropy item with the 'Foto' type. """

    type: str = "Foto"
    # TODO: recto/verso, size


@dataclass
class Blatt(Item):
    """ A representation of a Tropy item with the 'Blatt' type. """

    type: str = "Blatt"


@dataclass
class Aufgeklebt(Item):
    """ A representation of a Tropy item with the 'Aufgeklebt' type. """

    type: str = "Aufgeklebt"
