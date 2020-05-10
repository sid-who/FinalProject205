import requests
import urllib
import json

URL = "https://api.apify.com/v2/key-value-stores/moxA3Q0aZh5LosewB/records/LATEST?disableRedirect=true"

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

requests = requests.get(url = URL, headers=headers)

covid_dict = requests.json()

#print(covid_dict)

cases_by_state = covid_dict['casesByState']

#print(cases_by_state)

parsed_covid_data = {}

for i in range(len(cases_by_state)):
	#print(cases_by_state[i]['name'])
	parsed_covid_data[cases_by_state[i]['name']] = {
		'range' : cases_by_state[i]['range'],
		'casesReported' : cases_by_state[i]['casesReported'],
		'communityTransmission' : cases_by_state[i]['communityTransmission']
	}

#print(parsed_covid_data)