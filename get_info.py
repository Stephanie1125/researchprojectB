from urllib.request import urlopen
from bs4 import BeautifulSoup

# For practicing web crawling
# get a string of the text of content in the website

url1 = 'http://www.f.waseda.jp/tetsuya/researchprojects.html'
res = urlopen(url1)
html1 = res.read()
soup = BeautifulSoup(html1, "lxml")
content1 = soup.body.get_text().rstrip()

print(content1)
