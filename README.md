# JSONStreamWriter

Stream JSON-serializable python objects as JSON array in file.

Initialize with file object or filename.

Raises a SerializationError if you send it an object json or cjson cannot handle.
        
Tries to use cjson for serializing objects, because you wouldn't be needing a silly thing like this if you weren't handling big old objects.

Usage:

	import JSONStreamWriter.JSONStreamWriter as JSONStreamWriter 
	f = "foo.json" # or file-like object
	with JSONStreamWriter.ArrayWriter(f) as jstream:
		jstream.write({"this": "that"})
		jstream.write({"the": "other"})
		jstream.write({"hippie": "joe"})
		jstream.write({"facist":{"bullyboy":["me", "you", "them"]}})

... yields:

	[
		{
			"this": "that"
		},
		[
			"the",
			"other"
		],
		{
			"hippie": "joe"
		},
		{
			"facist": {
				"bullyboy": [
					"me",
					"you",
					"them"
				]
			}
		},
		[
			"a",
			"b"
		],
		[
			0,
			1,
			2
		]
	]
