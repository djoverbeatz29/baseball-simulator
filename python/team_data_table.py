import requests
from bs4 import BeautifulSoup
import pandas

page = requests.get("https://www.baseball-reference.com/leagues/MLB/2019-standard-batting.shtml")
soup = BeautifulSoup(page.content, 'html.parser')
my_table = soup.find('table')
my_head = my_table.find('thead')

# Old version, with renaming so as not to overwrite
# my_head_cells = [cell.text for cell in my_head.find_all('th')]
# my_rows = [row for row in my_table.find_all('tr')]
# my_cells = [[float(cell.text) for cell in row.find_all('td')] for row in my_rows]
# my_cells = [cell for cell in my_cells if cell]
# stats = pandas.DataFrame(data=my_cells, columns=my_head_cells[1:])
# stats = stats.iloc[:30, :]

my_head = [cell.text for cell in my_head.find_all('th')]
my_table = [row for row in my_table.find_all('tr')]
my_table = [[float(cell.text) for cell in row.find_all('td')] for row in my_table]
my_table = [cell for cell in my_cells if cell]
stats = pandas.DataFrame(data=my_table, columns=my_head[1:])
stats = stats.iloc[:30, :]

df = stats[['PA', 'H', '2B', '3B', 'HR', 'BB', 'GDP', 'HBP', 'SH', 'SF']]
df['1B'] = df['H'] - df[['2B', '3B', 'HR']].sum(1)
df['WALK'] = df[['BB', 'HBP']].sum(1)
df['OUT'] = df['PA'] - df[['H', 'WALK']].sum(1)
df_probs = df[['1B', '2B', '3B', 'HR', 'WALK', 'OUT']]
df_probs = df_probs.div(df_probs.sum(1), axis=0)
team1 = df_probs.sample(9)
avails = [ix for ix in df_probs.index if ix not in team1.index]
team2 = df_probs.iloc[avails, :].sample(9)