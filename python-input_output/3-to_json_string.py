#!/usr/bin/python3
import json


class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        try:
            return super().default(obj)
        except TypeError:
            return str(obj)  # Or other custom handling

def to_json_string(my_obj):
    return json.dumps(my_obj, cls=CustomJSONEncoder)
