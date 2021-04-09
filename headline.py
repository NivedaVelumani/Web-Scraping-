import requests
import bs4
res = requests.get("https://en.wikipedia.org/wiki/Machine_learning")
type(res)
soup = bs4.BeautifulSoup(res.text, "html.parser")
type(soup)
soup.select('.mw-headline')
for i in soup.select('.mw-headline'):
  print(i.text)
