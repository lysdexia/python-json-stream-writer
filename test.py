#!/usr/bin/env python
import JSONStream.JSONStream as JSONStream
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
    with JSONStream.ArrayWriter(f) as jstream:
        for obj in objects:
            jstream.write(obj)

    f = open("bar.json", "wb")
    with JSONStream.ArrayWriter(f) as jstream:
        for obj in objects:
            jstream.write(obj)

    # expect empty array
    f = "bat.json"
    with JSONStream.ArrayWriter(f) as jstream:
        try:
            jstream.write(set(["a", "a", "a"]))
        except JSONStream.SerializationError as error:
            print error

