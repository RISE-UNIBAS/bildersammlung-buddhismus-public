""" client.py

Client class. """

from __future__ import annotations
from scripts.items import Aufgeklebt, Blatt, Fotoblatt, Item
from scripts.transform import Transform, TransformFotoblatt, TransformContainer, TransformContainerVerso
from scripts.tropy import Tropy
import copy


class Client:
    """ Client to transform a loaded Tropy JSON export file. """

    @staticmethod
    def run_transformation(json_export: dict,
                           save_path: str) -> None:
        """ Transform a loaded Tropy JSON export file.

        'Makulatur' and 'Dubletten' items are skipped.

        :param json_export: loaded Tropy JSON export file
        :param save_path: complete path to save file including file extension
        """

        # TODO: add kwargs for properties to be skipped, {"Makulatur": list, "Dubletteb: "tag"})

        # load/validate/clone Tropy:
        original_tropy = Tropy(json_export=json_export)
        original_tropy.validate()
        new_tropy = copy.deepcopy(original_tropy)
        new_tropy.graph.clear()

        # load items from Tropy graph:
        for item in original_tropy.graph:

            # initialize item to be transformed from given Tropy item:
            item_to_transform = Item()
            item_to_transform.copy_metadata_from_dict(item)
            item_to_transform.list2metadata()

            # transform item according to type:
            try:
                # items to skip:
                if "Makulatur" in item_to_transform.list:
                    continue
                elif "Dubletten" in item_to_transform.tag:
                    continue
            except TypeError:
                try:
                    # items of type "Geheftete Blätter" with verso container:
                    if item_to_transform.title in ["Context_We_2_Nyanatilokas_Autobiographie_1267762_0005",
                                                     "Context_We_3_Nyanatiloka_1270875_0027"]:
                        transformer = TransformContainerVerso(Blatt)
                    # regular items of type "Geheftete Blätter":
                    elif item_to_transform.type == "Geheftete Blätter":
                        transformer = TransformContainer(Blatt)
                    # Nyanatiloka's passport is item of type "Klarsichtmappe" but requires special treatment:
                    elif item_to_transform.title in ["Context_We_3_Nyanatiloka_1270875_0061"]:
                        continue
                    # items of type "Klarsichtmappe" that require "Aufgeklebt":
                    elif item_to_transform.title in ["WE 1 Teil 2 0021"]:
                        transformer = TransformContainerVerso(Aufgeklebt)
                    # regular items of type "Klarsichtmappe":
                    elif item_to_transform.type == "Klarsichtmappe":
                        transformer = TransformContainer(Blatt)
                    # regular items of other types:
                    elif item_to_transform.type == "Fotoblatt":
                        transformer = TransformFotoblatt(Fotoblatt)
                    else:
                        transformer = Transform(Item.get_str_mapping()[item_to_transform.type])
                    transformer.run(item=item_to_transform)
                    # ingest into new Tropy graph:
                    new_tropy.graph.extend(transformer.serialize())
                except Exception:
                    raise

        # save Tropy:
        new_tropy.save(save_path)
