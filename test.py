import urllib.request
import json

# original sample from class notes
url = "https://data.cityofboston.gov/resource/awu8-dc52.json?$limit=10"
response = urllib.request.urlopen(url).read().decode("utf-8")
print(json.dumps(json.loads(response), sort_keys=True, indent=2))