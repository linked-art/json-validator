
import os
from json_schema_for_humans.generate import GenerationConfiguration, generate_from_filename

config = GenerationConfiguration(
	show_breadcrumbs=False,
	description_is_markdown=True,
	template_folder="./template",
	template_name="la")

entries = ['object', 'place', 'person', 'group', 'set', 'text', 'image', 'provenance', 'event', 'digital']

for s in entries:
	print(f"Building documentation for {s}")
	generate_from_filename(f"schema/{s}.json", f"html/{s}.html", config=config)

head = """
<link rel=stylesheet type=text/css href="https://fonts.googleapis.com/css?family=Overpass:300,400,600,800">
<script src=https://code.jquery.com/jquery-3.4.1.min.js integrity="sha256-CSXorXvZcTkaix6Yvo6HppcZGetbYMGWSFlBw8HfCJo=" crossorigin=anonymous></script>
<link href=https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css rel=stylesheet integrity=sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T crossorigin=anonymous>
<script src=https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js integrity=sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM crossorigin=anonymous></script>
<link rel=stylesheet type=text/css href=schema_doc.css>
<script src=https://use.fontawesome.com/facf9fa52c.js></script>
<script src=schema_doc.min.js></script>
<meta charset=utf-8><title>Linked Art Schema Definitions</title>
"""

fh = open('html/index.html', 'w')
fh.write(f'<html><head>{head}</head><body><h1>Linked Art Schema Definitions</h1><p><ul>')
for e in entries:
	fh.write(f"<li><a href=\"{e}.html\">{e}</a></li>")
fh.write('</ul></p></body></html>')
fh.close()


