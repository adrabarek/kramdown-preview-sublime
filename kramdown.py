from sublime_plugin import TextCommand
from sublime import Region
import tempfile
import os

HEADER = b"""<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
  <script id="MathJax-script" async
          src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
  </script>
</head>
<body>
"""

FOOTER = b"""</body>
</html>
"""

class RenderKramdownInBrowser(TextCommand):
	def run(self, edit):
		fn = self.view.file_name()

		content = ''
		with tempfile.NamedTemporaryFile() as f:
			f.write(bytes(self.view.substr(Region(0, self.view.size())), 'utf-8'))
			f.flush()
			stream = os.popen('kramdown ' + f.name)
			content = stream.read()				

		with tempfile.NamedTemporaryFile(delete=False, suffix='.html') as f:
			f.write(HEADER)
			f.write(bytes(content, 'utf-8'))
			f.write(FOOTER)
			f.flush()
			command = 'sensible-browser ' + f.name + '&'

		stream = os.popen(command)