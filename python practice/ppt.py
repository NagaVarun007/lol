import requests

# Define the URL
url = "https://mapi.makemytrip.com/clientbackend/entity/api/hotel/200706181440296181/flyfishReviews?srcClient=DESKTOP&contextType=null&language=eng&region=in&currency=INR&idContext=B2C&countryCode=IN"

# Define the payload (data to be sent in the request)
payload = {
    "filter": {
        "ota": "MMT"
    },
    "sortCriteria": {
        "sortBy": "Latest first"
    },
    "start": 0,
    "limit": 10000
}

# Define headers
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Referer": "https://www.makemytrip.com/"
    
}

# Make the POST request
response = requests.post(url, json=payload, headers=headers)

# Check if request was successful (status code 200)
if response.status_code == 200:


    # Extract data from the response
    data = response.json()
    
    # Process the data as needed
    print(data)  # Print or further process the data
else:
    print("Failed to fetch data. Status code:", response.status_code)

    