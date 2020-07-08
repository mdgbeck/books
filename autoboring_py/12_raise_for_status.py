import requests
res = requests.get('https://mdgbeck.com/recipes/template.html')

try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))
