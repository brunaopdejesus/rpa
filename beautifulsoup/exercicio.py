from bs4 import BeautifulSoup

html_doc = """
<html><body>
<p>Texto 1</p>
<p>Texto 2</p>
</body></html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

first_p = soup.p
next_p = first_p.findNextSibling('p')
print(next_p.text)

