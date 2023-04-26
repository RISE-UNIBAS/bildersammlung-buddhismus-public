""" client.py
=============
Client class. """

from __future__ import annotations
from scripts.items import Aufgeklebt, Blatt, Fotoblatt, Item
from scripts.metadata import Metadata
from scripts.transform import Transform, TransformFotoblatt, TransformContainer, TransformContainerVerso
from scripts.tropy import Tropy
from scripts.utility import Utility
import copy


class Client:
    """ Standalone client. """

    @staticmethod
    def run_transformation(json_export: dict,
                           save_path: str) -> None:
        """ Transform a loaded Tropy JSON export file from archival order to indexing.

        'Makulatur' and 'Dubletten' items are skipped.

        :param json_export: loaded Tropy JSON export file
        :param save_path: complete path to save file including file extension
        """

        # TODO: add kwargs for properties to be skipped, {"Makulatur": list, "Dubletten": "tag"})

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

    @staticmethod
    def run_analysis(json_export: dict,
                     save_dir: str,
                     *fields: str) -> None:
        """ Run analysis on Tropy fields in a loaded Tropy JSON export file and save analyses to CSV files.

        :param json_export: loaded Tropy JSON export file
        :param save_dir: path to save directory
        """

        for field in fields:
            if field == "person":
                Client.persons2csv(json_export=json_export, save_path=f"{save_dir}/{field}.csv")
            else:
                Client.parsed_field2csv(json_export=json_export,
                                        save_path=f"{save_dir}/{field}_inscribed.csv",
                                        field=field,
                                        inscribed=True)
                Client.parsed_field2csv(json_export=json_export,
                                        save_path=f"{save_dir}/{field}.csv",
                                        field=field,
                                        inscribed=False)

    @staticmethod
    def persons2csv(json_export: dict,
                    save_path: str) -> None:
        """ Extract persons from Tropy JSON export file to CSV file (name variants of one person in one row).

        Method (for now) limited to inscribed persons shown.

        :param json_export: loaded Tropy JSON export file
        :param save_path: complete path to save file including file extension
        """

        tropy = Tropy(json_export=json_export)
        persons = []
        for item in tropy.graph:
            parsed_item = Item()
            parsed_item.copy_metadata_from_dict(item)
            try:
                persons = persons + parsed_item.get_inscribed_persons()
            except TypeError:
                pass

        header = ["person_id", "inscribed_name", "source_identifier"]
        data = []
        for person in persons:
            for variant_name in person.variant_names:
                row = [person.identifier, variant_name.transcription]
                source_identifiers = [source.identifier for source in variant_name.sources]
                row.append(",".join(source_identifiers))
                data.append(row)

        Utility.save_csv(header=header,
                         data=data,
                         file_path=save_path)
        Metadata.person_id = 1

    @staticmethod
    def parsed_field2csv(json_export: dict,
                         save_path: str,
                         field: str,
                         inscribed: bool = False) -> None:
        """ Save parsed field from Tropy JSON export file to CSV file.

        :param json_export: loaded Tropy JSON export file
        :param save_path: complete path to save file including file extension
        :param field: the field to be parsed
        :param inscribed: toggle inscribed field, defaults to False
        """

        tropy = Tropy(json_export=json_export)
        header = [field, "source_identifier"]
        data = []
        for item in tropy.graph:
            parsed_item = Item()
            parsed_item.copy_metadata_from_dict(item)
            try:
                parsed_field = parsed_item.get_parsed_field(field=field,
                                                            inscribed=inscribed)
                if parsed_field is not None:
                    data = data + parsed_field
            except TypeError:
                pass

        Utility.save_csv(header=header,
                         data=data,
                         file_path=save_path)
