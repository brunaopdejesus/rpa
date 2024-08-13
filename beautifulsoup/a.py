from bs4 import BeautifulSoup

html_doc = """
<html><head><title>Título</title</head>
<body><a href="google.com">link</a>
<p class="titulo">Este é um parágrafo.</p>
<img src='a'></img>
</body></html>
"""

soup = BeautifulSoup(html_doc, 'lxml')

# title = soup.title
# print(title.text)

# p = soup.find('p', class_='titulo')
# print(p.text)

# soup = BeautifulSoup("<html><body>aaa</body></html>, 'html.parser'")
# print(soup.body)

links = soup.find_all('a')
for link in links:
    print(link.get('href'))

img = soup.find('img')
print(img['src'])