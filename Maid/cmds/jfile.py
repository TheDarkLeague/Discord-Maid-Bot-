#Credit function write_json to GeeksforGeeks
#https://www.geeksforgeeks.org/append-to-json-file-using-python/

import json

def open_jfile(filename):
    with open(filename, mode = 'r', encoding = 'utf8') as jfile_settings:
        jdata = json.load(jfile_settings)
        return jdata

def write_json(data, filename, indent = None):
    with open(filename, 'w') as jfile_settings:
        json.dump(data, jfile_settings, indent = indent)