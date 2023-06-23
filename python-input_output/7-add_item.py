#!/usr/bin/python3
import json
from sys import argv
import os

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

if os.path.exists("add_item.json"):
    old = load_from_json_file("add_item.json")
    for i in range(1, len(argv)):
        old.append(argv[i])
    save_to_json_file(old, "add_item.json")
else:
    new = []
    for i in range(1, len(argv)):
        new.append(argv[i])
    save_to_json_file(new, "add_item.json")
