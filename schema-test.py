
import json
import jsonschema
import os

from jsonschema import validate, Draft7Validator
from jsonschema.exceptions import ValidationError
import json


model_dirs = {
	"place": "place",
	"person": "person",
	"group": "group",
	"text": "text",
	"object": "object"
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
			print("-"*120)
			print("Processing: %s" % fn)
			fh = open(fn)
			data = json.load(fh)
			fh.close()

			errs = []
			for error in v.iter_errors(data):
				errs.append(error)
				# 	print(error.absolute_schema_path) <-- this is the current path through the schema 
				print(f"  /{'/'.join([str(x) for x in error.absolute_path])} --> {error.message} ")
			if not errs:
				print("  Validated!")
