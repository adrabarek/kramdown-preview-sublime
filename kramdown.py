'''
Sublime Text 3 plugin for previewing currently edited kramdown
document in a web browser.
'''

import os
from tempfile import NamedTemporaryFile

from sublime_plugin import TextCommand
from sublime import Region

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


class PreviewKramdown(TextCommand):
    '''Opens web browser and renders currently active document as kramdown.'''

    def run(self, _):
        content = ''
        with NamedTemporaryFile() as tmpfile:
            tmpfile.write(
                bytes(
                    self.view.substr(
                        Region(
                            0,
                            self.view.size())),
                    'utf-8'))
            tmpfile.flush()
            stream = os.popen('kramdown ' + tmpfile.name)
            content = stream.read()

        with NamedTemporaryFile(delete=False, suffix='.html') as tmpfile:
            tmpfile.write(HEADER)
            tmpfile.write(bytes(content, 'utf-8'))
            tmpfile.write(FOOTER)
            tmpfile.flush()
            command = 'sensible-browser ' + tmpfile.name + '&'

        stream = os.popen(command)
