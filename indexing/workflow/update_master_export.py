import datetime
import json
import os
import sys

DEBUG = True
indexes_to_update = ["title", "creator", "folder", "rights", "tag"]


def write_to_master_log(line, debug=False):
    if debug:
        print(line)

    with open('indexing/workflow/logs/master_log.txt', 'a') as file:
        file.write(line + "\n")


def read_export_jsons(usr_export_file_list):
    usr_export_list = []
    for user_file in usr_export_file_list:
        with open(f'user_exports/{user_file}', 'r') as file:
            usr_export_list.append(json.load(file))
    return usr_export_list


def update_master_export(user_data, master_data):
    text_to_log = []

    for item in user_data["@graph"]:
        if "identifier" in item:
            for master_item in master_data["@graph"]:
                if "identifier" in master_item:
                    if item["identifier"] == master_item["identifier"]:
                        for index in indexes_to_update:
                            if index in item:
                                try:
                                    if item[index] != master_item[index]:
                                        master_item[index] = item[index]
                                        text_to_log.append(f'>>>> Updating {item["identifier"]}: {index}')
                                    else:
                                        text_to_log.append(f'>>>> {item["identifier"]}: {index} is up to date')
                                # index missing in master_item:
                                except KeyError:
                                    master_item[index] = item[index]
                                    text_to_log.append(f'>>>> Adding {item["identifier"]}: {index}')

    write_to_master_log("\n".join(text_to_log), debug=DEBUG)


def write_export_json(master_data):
    text_to_log = []

    # List and open each json file in the 'to_download' folder
    for ufile in os.listdir('to_download'):
        text_to_log.append(f'>> Updating {ufile}')
        with open(f'to_download/{ufile}', 'r') as json_file:
            data = json.load(json_file)

        # Loop through each item in the json file
        for item in data['@graph']:
            # If the item has an identifier, check if it is in the master export
            if 'identifier' in item:
                for master_item in master_data['@graph']:
                    if 'identifier' in master_item:
                        if item['identifier'] == master_item['identifier']:
                            for index in indexes_to_update:
                                if index in master_item:
                                    if item[index] != master_item[index]:
                                        item[index] = master_item[index]
                                        text_to_log.append(f'>>>> Updating {item["identifier"]}: {index}')

        # Write the updated json file to the 'to_download' folder
        write_to_master_log("\n".join(text_to_log), debug=DEBUG)

        with open(f'to_download/{ufile}', 'w') as json_file:
            json.dump(data, json_file, indent=4)


if __name__ == '__main__':
    user_export_file_list = [f for f in os.listdir('indexing/workflow/user_exports') if f.endswith(".json")]

    if len(user_export_file_list) == 0:
        write_to_master_log('No new user exports found. Exiting...', debug=DEBUG)
        sys.exit()

    # Load the master export
    write_to_master_log('Loading master export...', debug=DEBUG)
    with open('export_master.json', 'r') as file:
        master_export = json.load(file)

    # Read all user supllied export jsons into a list
    write_to_master_log('Loading user exports...', debug=DEBUG)

    user_export_list = read_export_jsons(user_export_file_list)

    # Update the master export with the user supplied data
    write_to_master_log(f'Updating master export with {len(user_export_list)} changed files...', debug=DEBUG)
    index = 0
    for user_data in user_export_list:
        write_to_master_log(f'>> Checking {user_export_file_list[index]}', debug=DEBUG)
        update_master_export(user_data, master_export)
        # move the file to the archive folder
        os.rename(f'user_exports/{user_export_file_list[index]}',
                  f'export_archive/{user_export_file_list[index]}')
        index += 1

    # Write the master export to file
    write_to_master_log('Writing master export to file...', debug=DEBUG)
    with open('export_master.json', 'w') as file:
        json.dump(master_export, file, indent=4)

    # Write the data back to the user supplied jsons
    # (This is done to ensure that the static image paths in the user supplied jsons are correct)
    write_to_master_log('Writing user exports to file...', debug=DEBUG)
    write_export_json(master_export)

    # Write the last update time and user to the master log
    write_to_master_log(f'The last update was made on {datetime.datetime.now()} by {sys.argv[0]}')
