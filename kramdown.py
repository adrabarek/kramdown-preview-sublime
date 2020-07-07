import sublime_plugin
import os

TMP_DIR = '/tmp'

HEADER = """<!DOCTYPE html>
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

FOOTER = """</body>
</html>
"""

class cd:
		# A convenience class for changing working directory for a single
		# scope.

    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)

class HtmlShow(sublime_plugin.TextCommand):
	def run(self, edit):
		if not os.path.exists(TMP_DIR):
			os.makedirs(TMP_DIR)
			
		if self.view.file_name() != None:
			print(os.getcwd())
								
			with cd(TMP_DIR):
				fn = self.view.file_name()
				
				command = '/usr/local/bin/kramdown ' + os.path.abspath(fn)
				print(command)
				stream = os.popen(command)
				output = stream.read()
				print(output)

				html_path = TMP_DIR + "/" + os.path.basename(fn) + ".html"
				with open(html_path, 'w') as f:
					f.write(HEADER)
					f.write(output)
					f.write(FOOTER)

				command = 'sensible-browser ' + html_path + '&'
				stream = os.popen(command)