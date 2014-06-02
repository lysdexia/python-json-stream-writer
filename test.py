#!/usr/bin/env python
import JSONStreamWriter.JSONStreamWriter as JSONStreamWriter
import sys
if __name__ == "__main__":
    objects = [ 
            {"this": "that"},
            ["the", "other"],
            {"hippie": "joe"},
            {
                "facist":{
                    "bullyboy":[
                        "me",
                        "you",
                        "them"
                        ]
                }
            },
            list(set(["a","a","b"])),
            range(3),
    ]

    f = "foo.json"
    with JSONStreamWriter.ArrayWriter(f) as jstream:
        for obj in objects:
            jstream.write(obj)

    f = open("bar.json", "wb")
    with JSONStreamWriter.ArrayWriter(f) as jstream:
        for obj in objects:
            jstream.write(obj)

    # expect empty array
    f = "bat.json"
    with JSONStreamWriter.ArrayWriter(f) as jstream:
        try:
            jstream.write(set(["a", "a", "a"]))
        except JSONStreamWriter.SerializationError as error:
            print error

