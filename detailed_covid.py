import requests
import urllib
import json

URL = "https://covidtracking.com/api/states"

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

requests = requests.get(url = URL, headers=headers)

detailed_covid_data = requests.json()

## target model =>  [ { 'state' : string, 'positive' : int, 'death' : int, 'recovered' : int}, ]

#print(detailed_covid_data)

DetailedCovidData = {}

for i in range(len(detailed_covid_data)):
	DetailedCovidData[detailed_covid_data[i]['state']] = {
		'death': detailed_covid_data[i]['death'],
		'recovered' : detailed_covid_data[i]['recovered'],
		'negative' : detailed_covid_data[i]['negative'],
		'hospitalized' : detailed_covid_data[i]['hospitalized']
	}


#print(parsedCovidData)