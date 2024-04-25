import requests
import json

hotelID = 200706181440296181
url = f"https://mapi.makemytrip.com/clientbackend/entity/api/hotel/{hotelID}/flyfishReviews?srcClient=DESKTOP&contextType=null&language=eng&region=in&currency=INR&idContext=B2C&countryCode=IN"

payload = {
    "filter": {
        "ota": "MMT"
    },
    "sortCriteria": {
        "sortBy": "Latest first"
    },
    "start": 0,
    "limit": 2000
}

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Referer": "https://www.makemytrip.com/"
}

response = requests.post(url, json=payload, headers=headers)

if response.status_code == 200:
    data = response.json()
    reviews_data = []

    for review in data['payload']['response']['MMT']:
        review_text = review.get('reviewText')
        if review_text:  # Check if the review text exists
            reviews_data.append(review_text)

    with open('review_texts.json', 'w') as json_file:
        json.dump(reviews_data, json_file, indent=4)
else:
    print("Failed to fetch data. Status code:", response.status_code)
