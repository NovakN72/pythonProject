import requests
import json

# create a formatted string of the Python JSON object
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


response = requests.get(
    "https://api-server.dataquest.io/economic_data/countries?filter_by=region=Sub-Saharan%20Africa"
)
jprint(response.json())
