#Caution: this file parses all 20 million files, do not run until script is prepared!

import requests
import json

def fetch_data(offset):
    url = f"https://data.cityofnewyork.us/resource/jz4z-kudi.json?$limit=50000&$offset={offset}"
    response = requests.get(url)
    if response.status_code == 200:
        try:
            return response.json()
        except ValueError:
            print("Error: Unable to parse JSON data.")
            return []
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return []
        
all_data = []
offset = 0

while True:
    data = fetch_data(offset)
    if not data:
        break
    all_data.extend(data)
    offset += 50000
    print(f"Fetched {len(data)} records, total: {len(all_data)}")

print("Total records fetched:", len(all_data))

