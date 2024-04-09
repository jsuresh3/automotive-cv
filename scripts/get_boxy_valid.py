import requests

import requests
import json


url = "http://5.9.71.146/dqrtq7zmfsr4q59crcya/boxy_labels_train.json"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    with open('train.json', 'w') as file:
        json.dump(data, file, indent=4)
    print("JSON data saved successfully.")
else:
    print("Failed to fetch JSON data. Status code:", response.status_code)
