
import os
import json
import requests

from jsonschema import validate, Draft202012Validator
from jsonschema.exceptions import ValidationError
from jsonschema._utils import find_additional_properties

from referencing import Registry, Resource

schema_dir = "schema"
corefn = os.path.join(schema_dir, f"core.json")
fh = open(corefn)
core_json = json.load(fh)
fh.close()

schema = Resource.from_contents(core_json)
registry = Registry().with_resources(
    [
        ("https://linked.art/api/1.0/schema/core.json", schema),
        ("core.json", schema)
    ],
)


schemafn = os.path.join(schema_dir, f"person.json")
fh = open(schemafn)
schema = json.load(fh)
fh.close()
v = Draft202012Validator(schema, registry=registry)

instance = "https://lux.collections.yale.edu/data/person/68e84c09-5159-4f8b-ae5c-0c9145d3b6fe"

resp = requests.get(instance)
data = resp.json()

allow_underscore_props = True

print("-"*120)
print("Processing: %s" % instance)
errs = []
for error in v.iter_errors(data):
    if error.validator == 'additionalProperties':
        aps = []
        for ap in find_additional_properties(error.instance, error.schema):
            if ap[0] != '_':
                aps.append(ap)
        if not aps:
            continue
    errs.append(error)
    # 	print(error.absolute_schema_path) <-- this is the current path through the schema 
    print(f"  /{'/'.join([str(x) for x in error.absolute_path])} --> {error.message} ")
if not errs:
	print("  Validated!")
