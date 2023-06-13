#!/usr/bin/python3
"""Module: 7-add_item
This is a script that adds all arguments to a Python list.
Save them to a file.
"""


import json
import sys
import os.path

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

new_file = "add_item.json"
new_list = []

if os.path.exists(new_file) and os.path.getsize(new_file) > 0:
    new_list = load_from_json_file(new_file)

if len(sys.argv) > 1:
    for elem in sys.argv[1:]:
        new_list.append(elem)

save_to_json_file(new_list, new_file)
