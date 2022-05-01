# Нужно определить кто самый умный(intelligence) из трех супергероев- Hulk, Captain America, Thanos.
# Для определения id нужно использовать метод /search/name
# Токен, который нужно использовать для доступа к API: 2619421814940190.
# Все адреса для доступа к API должны начинаться с https://superheroapi.com/api/2619421814940190/.

import requests
from pprint import pprint


token = 2619421814940190
hero = ['Hulk', 'Captain America', 'Thanos']
url = f'https://www.superheroapi.com/api.php/{token}/search/{hero}'
intelligence = {}

for i in hero:
    url = f'https://www.superheroapi.com/api.php/{token}/search/{i}'
    data = requests.get(url)
    d = data.json()
    intel = int(d['results'][0]['powerstats']['intelligence'])
    if i in intelligence:
        intelligence[i] += [intel]
    else:
        intelligence[i] = [intel]
print(f'intelligence {intelligence}')
max_int = max(intelligence.values())
for k, v in intelligence.items():
    if v == max_int:
        print(f'самый умный из трех супергероев: {k}')
