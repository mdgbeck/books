#! python3
# searchpypi.py opens several search results.

import requests, sys, webbrowser, bs4
print('Searching...')

res = requests.get('https://pypi.org/search/?q=' + ' '.join(sys.argv[1: ]))
res.raise_for_status()

# retrieve top search result links
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# open new tab for each
link_elems = soup.select('.package-snippet')

num_open = min(5, len(link_elems))

for i in range(num_open):
    url = 'https://pypi.org' + link_elems[i].get('href')
    print('Opening ', url)
    webbrowser.open(url)
