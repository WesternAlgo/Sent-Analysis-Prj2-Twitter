import json
import requests
#from text_api_config import apikey

with open('tweetsList.txt', 'r') as file:
    data = file.read

headers = {
    "Content-Type": "application/json",
    "apikey": "7bd760c4-fd69-4d04-9bc0-d55bf2ea6dbc"
}
body = {
        "text": data
    }
url = "https://app.thetextapi.com/text/ner"
 
response = requests.post(url, headers=headers, json=body)
ner = json.loads(response.text)["ner"]
print(ner)