""" items.py
=============
Item classes. """

from __future__ import annotations
from dataclasses import dataclass, asdict
from scripts.person import InscribedName, Person, Source
from scripts.metadata import Metadata
from typing import List, Dict


@dataclass
class Item:
    """ A representation of a Tropy item.

    Parameter naming follows Tropy naming convention for fields (and not PEP).

    :param template: http://purl.org/dc/elements/1.1/type
    :param title: http://purl.org/dc/elements/1.1/title
    :param LocationCreated:
    :param LocationShown:
    :param PersonInImage:
    :param PersonInImageWDetails:
    :param creator: http://purl.org/dc/elements/1.1/creator
    :param dcterms_creator:
    :param date: http://purl.org/dc/elements/1.1/date
    :param dcterms_date:
    :param type: http://purl.org/dc/elements/1.1/type
    :param source: http://purl.org/dc/elements/1.1/source
    :param collection: https://tropy.org/v1/tropy#collection
    :param box: https://tropy.org/v1/tropy#box
    :param folder: https://tropy.org/v1/tropy#folder
    :param object: http://www.europeana.eu/schemas/edm/object
    :param identifier: http://purl.org/dc/elements/1.1/identifier
    :param rights: http://purl.org/dc/elements/1.1/rights
    :param hasPart: http://purl.org/dc/terms/hasPart
    :param isPartOf: http://purl.org/dc/terms/isPartOf
    :param isRelatedTo: http://www.europeana.eu/schemas/edm/isRelatedTo
    :param list: Tropy list
    :param photo: https://tropy.org/v1/tropy#photo
    :param tag: Tropy tag
    :param note: Tropy note
    """

    template: str = "https://tropy.org/v1/templates/id#iTbU0YBP"
    LocationCreated: str = None
    LocationShown: str = None
    PersonInImage: str = None
    PersonInImageWDetails: str = None
    title: str = None
    creator: str = None
    dcterms_creator: str = None
    date: str = None
    dcterms_date: str = None
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
    note: list = None

    @staticmethod
    def get_normalized_tropy_field_names() -> dict:
        """ Get normalized keys. """

        normalized_keys = {"dcterms:creator": "dcterms_creator",
                           "dcterms:date": "dcterms_date"}

        return normalized_keys

    def get_inscribed_persons(self) -> List[Person] | None:
        """ """
        try:
            assert self.PersonInImageWDetails is not None
            persons = []
            source = Source(identifier=self.identifier,
                            signature=self.source)
            inscribed_persons = self.PersonInImageWDetails.split(";")
            for inscribed_person in inscribed_persons:
                person = Person(identifier=Metadata.get_serialized_id("person_id"))
                Metadata.increment_id("person_id")
                print(person.identifier)
                names_variants = inscribed_person.split("|")
                for name_variant in names_variants:
                    inscribed_name = InscribedName(transcription=name_variant.strip())
                    if inscribed_name.sources is None:
                        inscribed_name.sources = [source]
                    else:
                        inscribed_name.sources.append(source)
                    if person.variant_names is None:
                        person.variant_names = [inscribed_name]
                    else:
                        person.variant_names.append(inscribed_name)
                persons.append(person)
            return persons
        except AssertionError:
            return None
        except:
            raise

    def list2metadata(self) -> None:
        """ Map (validated) list content to metadata fields. """

        try:
            if "Makulatur" in self.list:
                return None
            else:
                for item in self.list:
                    if "F" in item:
                        self.box = item
                    elif "J" in item:
                        self.folder = item
                    elif "A" in item:
                        self.object = item
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
                try:
                    normalized_key = self.get_normalized_tropy_field_names()[key]
                    self.__setattr__(normalized_key, dictionary[key])
                except KeyError:
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
