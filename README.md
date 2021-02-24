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

Output from the script is, for example:

```
------------------------------------------------------------------------------------------------------------------------
Processing: ../linked.art/content/example/person/12.json
  /member_of/0 --> 'id' is a required property 
  /member_of/0 --> Additional properties are not allowed ('member_of', 'classified_as' were unexpected) 
------------------------------------------------------------------------------------------------------------------------
Processing: ../linked.art/content/example/person/13.json
  Validated!
```


## Documentation Generator

Install the generator:

`pip install json-schema-for-humans`

Run the generator:

`generate-schema-doc --config no_show_breadcrumbs --config description_is_markdown --config template_folder=$PWD/template --config template_name=la schema/object.json html/object.html`

The options I use:

* `no_show_breadcrumbs`: this prevents it from showing the path through the schema at each stage. We don't care about the structure of the schema in the API docs.
* `description_is_markdown`: parses the `description` field in the schemas as markdown not plain text, allowing links and basic formatting
* `template_folder` is where templates are available
* `template_name` is the name of the template within the above folder (another directory, with the HTML, CSS and JS files in it)

