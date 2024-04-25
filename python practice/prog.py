import requests
import json
from datetime import datetime

hotelID = 2562673241805735043

reviews_data = {
    "otaPId": hotelID,
    # "name": hotelName,
    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "reviews": []
}

offset = 0
limit = 50
i = 0

while True:
    url = f'https://ugcx.goibibo.com/api/HotelReviews/forMobileV4/{hotelID}?offset={offset}&limit={limit}&sortBy=help&webp=true&flavour=dWeb'
    headers = {
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    }

    response = requests.get(url, headers= headers)
    response_content = response.json()

   

    # with open('review_raw.json','w') as json_file:
    #     json.dump(response_content, json_file, indent = 4)

    data_slot = response_content['reviews']
    
    
    
    if not data_slot:
        break  
    
    for data in data_slot:
        reviewId = data.get('id')
        hotelName = data.get('hotelName')
        hotelCity = data.get('hotelCity')
        reviewContent = data.get('reviewContent')
        
        reviews_data['reviews'].append({
            "reviewId": i,
            "reviewContent": reviewContent
        })
        i=i+1
    offset += limit

with open('CaravelaResort.json', 'w') as json_file:
    json.dump(reviews_data, json_file, indent=4) 