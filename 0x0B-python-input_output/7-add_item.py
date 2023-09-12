#!/usr/bin/python3

"""
Module 7-add_item docs

Script adds all commandline arguments to a
python list and save them to a text file

Uses functions save_to_json_file and load_from_json_file
from modules 5-save_to_json_file and 6-load_from_json_file

Saves the json output to add_item.json
"""


if __name__ == "__main__":

    import sys
    import json
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file')\
        .load_from_json_file

    filename = "add_item.json"

    try:
        result = load_from_json_file(filename)
    except (FileNotFoundError, json.decoder.JSONDecodeError) as e:
        result = []

    for arg_idx in range(len(sys.argv)):
        if arg_idx == 0:
            continue
        result.append(sys.argv[arg_idx])

    save_to_json_file(result, filename)
