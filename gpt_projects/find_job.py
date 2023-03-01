import requests
from bs4 import BeautifulSoup

# Send a GET request to the website and get the HTML response
url = 'https://onepiece.fandom.com/wiki/Episode_List'
response = requests.get(url)
html = response.content

# Use BeautifulSoup to parse the HTML and extract the list of episodes
soup = BeautifulSoup(html, 'html.parser')
table = soup.find('table', class_='wikitable')
rows = table.find_all('tr')[1:]
episodes = []

for row in rows:
    cells = row.find_all('td')
    episode = {
        'number': cells[0].get_text().strip(),
        'title': cells[1].get_text().strip(),
        'airdate': cells[2].get_text().strip(),
    }
    episodes.append(episode)

# Print the list of episodes
for episode in episodes:
    print(f"{episode['number']}: {episode['title']} ({episode['airdate']})")
