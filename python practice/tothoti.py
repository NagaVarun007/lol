import requests
import json

cityname = input("Enter name of the city: ")

# Getting city code
url = f'https://mapi.goibibo.com/autosuggest/v5/search?language=eng&region=in&q={cityname}&z=false&brand=GI&exps=expscore2&exp=4'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}
response = requests.get(url, headers=headers)
response_content = response.json()

citycode = response_content[0].get('voyId')


hotel_details = []

url = f'https://hermes.goibibo.com/hotels/v13/search/data/v3/{citycode}/20240427/20240428/1-2-0/then?s=popularity&cur=INR&locusData=%7B%22id%22%3A%22CTXWA%22%2C%22type%22%3A%22city%22%2C%22cityCode%22%3A%22CTXWA%22%2C%22countryCode%22%3A%22IN%22%7D&next=202201221730541839__5&tmz=-330'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}
response = requests.get(url, headers=headers)
response_content = response.json()
hotel_details.append(response_content)


'''
    hotel_details.append({
        'hotelName': hotel.get('hn'),
        'hotelCode': hotel.get('hc'),
        'starCategory': hotel.get("hr"),
        'location': hotel.get('l'),
        'image': hotel.get('t'),
        'about': hotel.get('cc'),
        'amenities': hotel.get('amu'),
        'price': hotel.get('spr'),
        'ratingScore': hotel.get('gr'),
        'reviewCount': hotel.get('grc'),
    })
'''
with open('allcity.json', 'w') as json_file:
    json.dump(hotel_details, json_file, indent=4)

