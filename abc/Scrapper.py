import requests
from bs4 import BeautifulSoup
req = requests.get("https://www.imdb.com/search/title/?release_date=2018-01-01,2018-12-31&sort=num_votes,desce")
soup = BeautifulSoup(req.content, "html.parser")
res = soup.title
print(res.get_text())