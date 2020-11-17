import requests
from bs4 import BeautifulSoup
import pandas

page = requests.get("https://www.baseball-reference.com/leagues/MLB/2019-standard-batting.shtml")
soup = BeautifulSoup(page.content, 'html.parser')
my_table = soup.find('table')
my_rows = [row for row in my_table.find_all('tr')]
my_cells = [[float(cell.text) for cell in row.find_all('td')] for row in my_rows]
my_cells = [cell for cell in my_cells if cell]
print(pandas.DataFrame(my_cells))