
import json
import jsonschema
import os

from jsonschema import validate, Draft7Validator
from jsonschema.exceptions import ValidationError
import json


model_dirs = {
	"place": "place",
	"person": "person"
}

base_instance_dir = "../linked.art/content/example"
schema_dir = "schema"



for (k,v) in model_dirs.items():

	schemafn = os.path.join(schema_dir, f"{v}.json")
	fh = open(schemafn)
	schema = json.load(fh)
	fh.close()
	v = Draft7Validator(schema)

	exampledir = os.path.join(base_instance_dir, k)
	files = os.listdir(exampledir)
	for f in files:
		if f.endswith('.json'):
			fn = os.path.join(exampledir, f)
			print("processing file: %s" % fn)
			fh = open(fn)
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
			print("validated!")
