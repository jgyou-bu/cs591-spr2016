import urllib.request
import urllib.parse
import json

'''
# original sample from class notes
url = "https://data.cityofboston.gov/resource/awu8-dc52.json?$limit=10"
response = urllib.request.urlopen(url).read().decode("utf-8")
print(json.dumps(json.loads(response), sort_keys=True, indent=2))
'''

# food pantry query
url2 = "https://data.cityofboston.gov/resource/vjvb-2kg6.json?area=boston"
response2 = urllib.request.urlopen(url2).read().decode("utf-8")
boston_pantries = json.loads(response2)
# prints out one row of table in unfriendly format
print(boston_pantries[0])

# prints out json in friendly format
print(json.dumps(json.loads(response2), sort_keys=True, indent=4))

#employee earnings
url4 = "https://data.cityofboston.gov/resource/wypd-uw2t.json?title=" + urllib.parse.quote_plus("Admin Secretary")
response4 = urllib.request.urlopen(url4).read().decode("utf-8")
employees = json.loads(response4)
print(employees)


# building energy and water use metrics
url3 = "https://data.cityofboston.gov/resource/n9us-mq2b.json"
