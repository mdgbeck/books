import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()

play_file = open('RomeoAndJulite.txt', 'wb')
for chunk in res.iter_content(100000):
    play_file.write(chunk)

play_file.close()
