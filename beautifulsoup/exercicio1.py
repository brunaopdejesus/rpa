from bs4 import BeautifulSoup

html_doc = """
<html><body>
<p>Texto 1</p>
<a href="#">Link</a>
<p>Texto 2</p>
</body></html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')
