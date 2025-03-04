import os
import requests
import json

# set API URL
url = "https://materials.hybrid3.duke.edu/materials/datasets/?page=1&page_size=3000"

# set the file save path in your computer
save_dir = r"E:\H3"  
file_name = "all_datasets_data.json"

# create folder
os.makedirs(save_dir, exist_ok=True)

# combine the pat
file_path = os.path.join(save_dir, file_name)

# send GET request
response = requests.get(url)

# check the GET request work
if response.status_code == 200:
    data = response.json()
    # save data to aimed location
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    print(f"data have been successfully download and save in {file_path}")
else:
    print("require faliure, tatus_code:", response.status_code)
