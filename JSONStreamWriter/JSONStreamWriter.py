#!/usr/bin/env python
"""
stream json-serializable python objects as json array in file

initialize with file object or filename


 Usage:
        import JSONStreamWriter.JSONStreamWriter as JSONStreamWriter

        f = "foo.json" # or file-like object
        with JSONStreamWriter.ArrayWriter(f) as jstream:
            jstream.write({"this": "that"})
            jstream.write({"the": "other"})
            jstream.write({"hippie": "joe"})
            jstream.write({"facist":{"bullyboy":["me", "you", "them"]}})
        
trys to use cjson for writing, because C.
"""
try:
    import cjson as json
    json.dumps = json.encode
except ImportError:
    import json

import sys

class ArrayWriter(object):
    """
    accepts a file path or a file like object
    writes the output as a json array
    in file

    """
    def __init__(self, o):

        if isinstance(o, file):
            self.obj = o

        if isinstance(o, str):
            self.obj = open(o, "wb")

    def __enter__(self):
        """
        bound input with open square bracket
        """
        self.obj.write("[")
        return self

    def __exit__(self, _type, value, traceback):
        """
        bound input with close square bracket, then close the file
        """
        self.obj.write("]")
        self.obj.close()

    def write(self, obj):
        """
        writes the first row, then overloads self with delimited_write
        """
        try:
            self.obj.write(json.dumps(obj))
            setattr(self, "write", self.delimited_write)
        except:
            self.bad_obj(obj)

    def delimited_write(self, obj):
        """
        prefix json object with a comma
        """
        try:
            self.obj.write("," + json.dumps(obj))
        except:
            self.bad_obj(obj)

    def bad_obj(self, obj):
        raise SerializationError("%s object not not serializable"%type(obj))
 
class SerializationError(Exception):
    def __init__(self, value):
        self.value = value 

    def __str__(self):
        return repr(self.value) 
