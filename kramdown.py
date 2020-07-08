import sublime_plugin
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

class RenderKramdownInBrowser(sublime_plugin.TextCommand):
	def run(self, edit):
		fn = self.view.file_name()

		command = 'kramdown ' + os.path.abspath(fn)
		stream = os.popen(command)
		output = stream.read()

		with tempfile.NamedTemporaryFile(delete=False, suffix='.html') as f:
			f.write(HEADER)
			f.write(bytes(output, 'utf-8'))
			f.write(FOOTER)
			command = 'sensible-browser ' + f.name + '&'

		stream = os.popen(command)