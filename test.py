import requests
import json


url = "https://api.tfl.gov.uk/StopPoint/490009333W/Arrivals"

response = requests.get(url)
response_as_object = json.loads(response.text)

print(response.text)
