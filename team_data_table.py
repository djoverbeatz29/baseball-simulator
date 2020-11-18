import requests
from bs4 import BeautifulSoup
import pandas

page = requests.get("https://www.baseball-reference.com/leagues/MLB/2019-standard-batting.shtml")
soup = BeautifulSoup(page.content, 'html.parser')
my_table = soup.find('table')
my_head = my_table.find('thead')
my_head_cells = [cell.text for cell in my_head.find_all('th')]
my_rows = [row for row in my_table.find_all('tr')]
my_cells = [[float(cell.text) for cell in row.find_all('td')] for row in my_rows]
my_cells = [cell for cell in my_cells if cell]
myDataFrame = pandas.DataFrame(data=my_cells, columns=my_head_cells[1:])
print(myDataFrame)