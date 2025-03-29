import requests
import json
import os

SAVE_FILE = "data_backup.json"
OFFSET_FILE = "last_offset.txt"

def fetch_data(offset):
    """Fetch data from API with pagination"""
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

def load_existing_data():
    """Load previously saved data if available"""
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:
            return json.load(f)
    return []

def load_last_offset():
    """Retrieve last offset from file"""
    if os.path.exists(OFFSET_FILE):
        with open(OFFSET_FILE, "r") as f:
            return int(f.read().strip())
    return 0  # Start from 0 if no offset file

def save_progress(data, offset):
    """Save fetched data and current offset"""
    with open(SAVE_FILE, "w") as f:
        json.dump(data, f)
    with open(OFFSET_FILE, "w") as f:
        f.write(str(offset))

# Load previous progress
all_data = load_existing_data()
offset = load_last_offset()

# Resume fetching
while True:
    data = fetch_data(offset)
    if not data:
        break
    all_data.extend(data)
    offset += 50000
    save_progress(all_data, offset)
    print(f"Fetched {len(data)} records, total: {len(all_data)}")

print("Total records fetched:", len(all_data))
