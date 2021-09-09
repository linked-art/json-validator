
import os
from json_schema_for_humans import generate
from json_schema_for_humans.generate import GenerationConfiguration, generate_from_filename, TEMPLATE_FILE_NAME

config = GenerationConfiguration(
	show_breadcrumbs=False,
	description_is_markdown=True,
	template_folder="./template",
	template_name="la")
TEMPLATE_FILE_NAME = "base_nohtml.html"
generate.TEMPLATE_FILE_NAME = TEMPLATE_FILE_NAME

entries = ['object', 'place', 'person', 'group', 'set', 'text', 'image', 'provenance', 'event', 'digital']

header = """---
title: "Linked Art Schema: {{title}}"
up_href: "/api/1.0/"
up_label: "Linked Art API 1.0"
---
"""

for s in entries:
	print(f"Building documentation for {s}")
	generate_from_filename(f"schema/{s}.json", f"html/{s}.html", config=config)
	# Jinja loses the linebreaks, so write markdown header in by hand
	fh = open(f'html/{s}.html')
	data = fh.read()
	fh.close()
	out = header.replace('{{title}}', s.title()) + "\n" + data
	fh = open(f'html/{s}.html', 'w')
	fh.write(out)
	fh.close()

# Can GET info from https://spinup.internal.yale.edu/api/v2/storage/5446
#os.system("aws s3 --profile linked-data.yalespace.org sync html s3://linked-data.yalespace.org/docs/model/")
#os.system("aws cloudfront --profile linked-data.yalespace.org create-invalidation --distribution-id E1CKFKVC1UT9DM --paths \"/*\"")

