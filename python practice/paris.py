import requests
import json

url = f'https://ugcx.goibibo.com/api/HotelReviews/forMobileV4/1585977246363947094?offset=0&limit=5&sortBy=help&webp=true&flavour=dWeb'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
response_content = response.json()

hotel_info = []

for review in response_content.get('reviews'):
    hotel_info.append({
        'hotelName': review.get('hotelName'),
        'hotelCity': review.get('hotelCity'), 
        'totalRating': review.get('totalRating'),
        'image_url': review.get('image_url'),
        'reviewContent': review.get('reviewContent')
    })

print(hotel_info)


with open('parisnovo_all.json', 'w') as json_file:
    json.dump(hotel_info, json_file, indent=4)