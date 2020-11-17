import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.baseball-reference.com/leagues/MLB/2019-standard-batting.shtml")
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.find('table'))