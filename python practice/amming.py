
import requests
import json
from datetime import datetime

hotelID = 4251924102367982860

reviews_data = {
    "otaPId": hotelID,
    # "name": hotelName,
    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "reviews": []
}


offset = 0
limit = 50

while True:
    url = f"https://ugcx.goibibo.com/api/HotelReviews/forMobileV4/{hotelID}?offset={offset}&limit={limit}"

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
            "reviewId": reviewId,
            "reviewContent": reviewContent
        })

    offset += limit

with open('Novotel_reviews_all.json', 'w') as json_file:
    json.dump(reviews_data, json_file, indent=4)