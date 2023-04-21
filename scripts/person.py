""" person.py
=============
Person class. """

from __future__ import annotations
from dataclasses import dataclass
from typing import List


@dataclass
class Person:
    """ Representation of a person.

    :param identifier: running person id, defaults to 1
    :param preferred_name: person's preferred name
    :param variant_names: person's variant names
    """

    identifier: str = None
    preferred_name: Name = None
    variant_names: List[Name | InscribedName] = None
    # TODO: add connection to norm data, e.g. GND


@dataclass
class Name:
    """ Representation of a name.

    :param anker:
    """

    anker: InscribedName = None
    # TODO: add name parts such as given name(s), family name, title


@dataclass
class InscribedName:
    """ Representation of an inscribed name.

    :param normalization:
    """

    sources: List[Source] = None
    transcription: str = None
    normalization: Name = None


@dataclass
class Source:
    """ Representation of a source.

    A source is any object in indexing/indexing.tpy.

    :param identifier:
    :param signature:
    """

    identifier: str = None
    signature: str = None
