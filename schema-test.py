
import json
import jsonschema
import os

from jsonschema import validate, Draft6Validator
from jsonschema.exceptions import ValidationError
import json


fh = file('schema/schema-core.json')
schema = json.load(fh)
fh.close()
v = Draft6Validator(schema)

files = os.listdir('../linked.art/content/example/object/')
for f in files:
	if f.endswith('.json'):
		fn = os.path.join('../linked.art/content/example/object/', f)
		print "processing file: %s" % fn
		fh = file(fn)
		data = json.load(fh)
		fh.close()
		try:
			v.validate(data)
		except ValidationError as e:
			print("Failed to validate %s" % fn)
			if e.absolute_schema_path[-1] == u'required' and \
				e.message.startswith("u'type'"):
				continue

			print(e.message)
			print(e.absolute_schema_path)
			print(e.absolute_path)
			break
		print "validated!"

