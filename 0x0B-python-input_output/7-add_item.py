#!/usr/bin/python3
import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


my_list = []
for item in range(1, len(sys.argv)):
    my_list.append(sys.argv[item])
try:
    obj = load_from_json_file("add_item.json")
    new_list = obj + my_list
    save_to_json_file(new_list, "add_item.json")
except Exception:
    save_to_json_file(my_list, "add_item.json")
