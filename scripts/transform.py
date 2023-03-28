""" transform.py
=============
Transform class. """

from __future__ import annotations
from typing import Dict, List, Type
from scripts.items import Item, Fotoblatt, Foto, Blatt
from scripts.metadata import Metadata
import re


class Transform:
    """ Transform Tropy item.

    :param target_class: the target class of the transformed item
    :param target: the instantiated target class
    """

    def __init__(self,
                 target_class: Type[Item],
                 target: Item = None) -> None:
        self.target_class = target_class
        self.target = target
        self.setup()

    def setup(self):
        if self.target is None:
            self.target = self.target_class()

    def run(self, item: Item) -> None:
        """ Run transformation, validation, etc. on Tropy item.

        :param item: item to be transformed
        """

        self.transform(item)
        self.validate(item)

    def transform(self, item: Item) -> None:
        """ Transform Tropy item.

        :param item: item to be transformed
        """

        for photo in item.photo:
            if re.search("^Context_", photo["filename"]) is not None:
                if self.target.photo is None:
                    self.target.transform(item=item,
                                          photo=photo,
                                          identifier=Metadata.get_serialized_id(f"{self.target.type.lower()}_id"))
                    Metadata.increment_id(f"{self.target.type.lower()}_id")
                else:
                    self.target.photo.append(photo)

    def validate(self, item: Item):
        """ Validate transformation.

        :param item: item to be transformed
        """

        pass

    def serialize(self) -> List[Dict]:
        """ Serialize transformed item(s). """

        return [self.target.serialize()]


class TransformContainer(Transform):
    """ Transform Tropy item that are opaque containers.

    Examples of opaque containers are items with type 'Klarsichtmappe' or 'Geheftete Blätter' type.

    :param target_class: the target Fotoblatt class of the transformed item
    :param contents: content items
    :param content_counter: content items seen
    """

    def __init__(self,
                 target_class: Type[Item],
                 contents: list = None,
                 content_counter: int = 0) -> None:
        super().__init__(target_class)
        self.contents = contents
        self.content_counter = content_counter
        self.setup()

    def setup(self):
        self.contents = []

    def transform(self, item: Item) -> None:
        """ Transform an opaque container Tropy item.

        Item is split into multiple content items typed by the target class class parameter.

        :param item: item to be transformed
        """

        relations = []
        for photo in item.photo:

            if re.search("^Containers_", photo["filename"]) is not None:
                if self.content_counter % 2 == 0:
                    target = self.target_class()
                    target.transform(item=item,
                                     photo=photo,
                                     identifier=Metadata.get_serialized_id("blatt_id"))
                    Metadata.increment_id("blatt_id")
                    relations.append(target.identifier)
                    self.contents.append(target)
                else:
                    self.contents[-1].photo.append(photo)

                self.content_counter += 1

        # assign relations:
        for content in self.contents:
            content.isRelatedTo = "; ".join(relations)

    def validate(self, item: Item):
        """ Validate transformation.

        :param item: item to be transformed
        """

        try:
            # number of items created:
            assert len(self.contents) == (len(item.photo) / 2) - 1

            for content in self.contents:
                # number of photos added:
                assert len(content.photo) == 2
                # number of relationships:
                assert len(content.isRelatedTo.split(";")) == len(self.contents)

        except AssertionError:
            print(f"ERROR: {item.type} item titled '{item.title}' not transformed correctly!")

    def serialize(self) -> List[Dict]:
        """ Serialize transformed item(s). """

        return [content.serialize() for content in self.contents]


class TransformContainerVerso(TransformContainer):
    """ TransfromContainer for item with only verso photos.

    Item is split into multiple content items typed by the target class attribute.

    :param target_class: the target Fotoblatt class of the transformed item
    :param contents: content items
    """

    def __init__(self,
                 target_class: Type[Item],
                 contents: list = None) -> None:
        super().__init__(target_class, contents)

    def transform(self, item: Item) -> None:
        """ TransfromContainer for items with only verso photos.

        :param item: item to be transformed
        """

        relations = []
        for photo in item.photo:

            if re.search("^Containers_", photo["filename"]) is not None:
                target = self.target_class()
                target.transform(item=item,
                                 photo=photo,
                                 identifier=Metadata.get_serialized_id("blatt_id"))
                Metadata.increment_id("blatt_id")
                relations.append(target.identifier)
                self.contents.append(target)

        # assign relations:
        for content in self.contents:
            content.isRelatedTo = "; ".join(relations)

    def validate(self, item: Fotoblatt):
        """ Validate transformation.

        :param item: item to be transformed
        """

        try:
            # number of items created:
            assert len(self.contents) == (len(item.photo)) - 2

            for content in self.contents:
                # number of photos added:
                assert len(content.photo) == 1
                # number of relationships:
                assert len(content.isRelatedTo.split(";")) == len(self.contents)

        except AssertionError:
            print(f"ERROR: {item.type} item titled '{item.title}' not transformed correctly!")


class TransformFotoblatt(Transform):
    """ Transform Tropy item with 'Fotoblatt' type.

     :param target: the target Fotoblatt class of the transformed item
     :param target: the instantiated Fotoblatt class
     :param fotos: 'Foto' items
     :param foto_counter: items of type 'Foto' seen """

    def __init__(self,
                 target_class: Type[Fotoblatt],
                 target: Fotoblatt = None,
                 fotos: list = None,
                 foto_counter: int = 0) -> None:
        super().__init__(target_class, target)
        self.fotos = fotos
        self.foto_counter = foto_counter
        self.setup()

    def setup(self):
        if self.target is None:
            self.target = Fotoblatt()
        self.fotos = []

    def transform(self, item: Fotoblatt) -> None:
        """ Transform Tropy item with 'Fotoblatt' type.

        Item is split into one item of type 'Fotoblatt' and multiple items of type 'Foto'.

        :param item: item to be transformed
        """
        for photo in item.photo:

            # create Fotoblatt:
            if re.search("^Context_", photo["filename"]) is not None:

                if self.target.photo is None:
                    self.target.transform(item=item,
                                          photo=photo,
                                          identifier=Metadata.get_serialized_id("fotoblatt_id"))
                    Metadata.increment_id("fotoblatt_id")
                else:
                    self.target.photo.append(photo)

            # create Fotos:
            if re.search("^Images_", photo["filename"]) is not None:
                if self.foto_counter % 2 == 0:
                    foto = Foto()
                    foto.transform(item=item,
                                   photo=photo,
                                   identifier=Metadata.get_serialized_id("foto_id"))
                    Metadata.increment_id("foto_id")

                    # assign relations for both Fotoblatt/Foto:
                    foto.isPartOf = self.target.identifier
                    try:
                        self.target.hasPart = self.target.hasPart + f"; {foto.identifier}"
                    except TypeError:
                        self.target.hasPart = f"{foto.identifier}"

                    # clean up:
                    self.fotos.append(foto)
                else:
                    self.fotos[-1].photo.append(photo)

                self.foto_counter += 1

    def validate(self, item: Fotoblatt):
        """ Validate transformation.

        :param item: item to be transformed
        """

        try:
            # number ob Fotoblatt and Foto items created:
            assert len(self.fotos) == (len(item.photo) / 2) - 1

            # number of photos added to Foto resp. Fotoblatt
            for foto in self.fotos:
                assert len(foto.photo) == 2
            assert len(self.target.photo) == 2

            # number of relationships:
            assert len(self.target.hasPart.split(";")) == len(self.fotos)

        except AssertionError:
            print(f"ERROR: '{item.type}' item titled '{item.title}' not transformed correctly!")

    def serialize(self) -> List[Dict]:
        """ Serialize transformed item(s). """

        return [foto.serialize() for foto in self.fotos] + [self.target.serialize()]
