import requests
import urllib
import json

URL = "https://covidtracking.com/api/states"

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

requests = requests.get(url = URL, headers=headers)

detailed_covid_data = requests.json()

## target model =>  [ { 'state' : string, 'positive' : int, 'death' : int, 'recovered' : int}, ]

#print(detailed_covid_data)

parsedCovidData = []

print(detailed_covid_data[0]['state'])

# for data in detailed_covid_data:
# 	temp_dict = {}
# 	temp_dict['state'] = detailed_covid_data[data['state']]
# 	temp_dict['positive'] = detailed_covid_data[data['positive']]
# 	temp_dict['death'] = detailed_covid_data[data['death']]
# 	temp_dict['recovered'] = detailed_covid_data[data['recovered']]
# 	parsedCovidData.append(temp_dict)
