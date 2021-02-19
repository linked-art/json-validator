# json-validator

json-schema validation of linked.art resources

## Validation

`schema-test.py` shows how to validate records:

In particular:
```
# load the appropriate schema json into schema here
v = Draft7Validator(schema)
# load the appropriate instance json into data here
errs = []
for error in v.iter_errors(data):
	errs.append(error)
	print(f"  /{'/'.join([str(x) for x in error.absolute_path])} --> {error.message} ")
if not errs:
	print("Validated!")
```

## Documentation Generator

Install the generator:

`pip install json-schema-for-humans`

Run the generator:

`generate-schema-doc --config no_show_breadcrumbs --config description_is_markdown schema/object.json html/object.html`

The options I use:

* `no_show_breadcrumbs`: this prevents it from showing the path through the schema at each stage. We don't care about the structure of the schema in the API docs.
* `description_is_markdown`: parses the `description` field in the schemas as markdown not plain text, allowing links and basic formatting

