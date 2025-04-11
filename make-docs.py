
import os
from json_schema_for_humans.generate import GenerationConfiguration, generate_from_filename
from json_schema_for_humans.generation_configuration import GenerationConfiguration

#config = GenerationConfiguration(
#	show_breadcrumbs=False,
#	description_is_markdown=True,
#	template_folder="./template",
#	template_name="la")
#TEMPLATE_FILE_NAME = "base_nohtml.html"
#generate.TEMPLATE_FILE_NAME = TEMPLATE_FILE_NAME


config=GenerationConfiguration(show_breadcrumbs=False, description_is_markdown=True,custom_template_path="template/la/base_nohtml.html")


entries = ['object', 'place', 'person', 'group', 'set', 'text', 'image', 'provenance', 'event', 'digital', 'abstract', 'concept']
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
