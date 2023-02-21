""" items.py

Metadata class. """

from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Metadata:
    """ A representation of project metadata. """

    aufgeklebt_id = 1
    blatt_id = 1
    foto_id = 1
    fotoblatt_id = 1

    @classmethod
    def get_type_mapping(cls):
        """ Get mapping of type qua attribute to short attribute name."""

        return {"aufgeklebt_id": "A",
                "blatt_id": "B",
                "foto_id": "F",
                "fotoblatt_id": "FB",
                }

    @classmethod
    def get_folder_mapping(cls):
        """ Get mapping of folder ID to short name. """

        return {"F01": "Moderner Buddhismus Europa Asien 1",
                "F02": "Moderner Buddhismus Europa Asien 2",
                "F03": "Nyanatilokas Autobiographie",
                "F04": "Nyanatilokas Nachlass",
                "F05": "Deutsche Buddhisten",
                "F06": "Moderner Buddhismus",
                "F07": "Moderner Buddhismus 3",
                "F08": "Govinda",
                "F09": "Neumann",
                }

    @classmethod
    def get_transformation_mapping(cls):
        """ Get mapping of Tropy archival order to Tropy enrichment projects. """

        return {

        }

    @classmethod
    def increment_id(cls, identifier: str) -> None:
        """ Increment identifier by 1.

        :param identifier: the identifier
        """

        setattr(cls, identifier, getattr(cls, identifier) + 1)

    @classmethod
    def get_serialized_id(cls, identifier: str) -> str:
        """ Get serialized identifier.

        :param identifier: the identifier
        """

        return f"{cls.get_type_mapping()[identifier]}{getattr(cls, identifier):04d}"
