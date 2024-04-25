import requests

voyID = 7668653265335023650

url = f'https://hermes.goibibo.com/hotels/v13/search/data/v3/{voyID}/20240424/20240425/1-2-0'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
response_content = response.json()

hotel_names = []

for hotel in response_content.get('data'):
    hotel_names.append(hotel.get('hn'))

print(hotel_names)

