#
# Code by Gurpreet Sidhu, Jose Perez, Cesar Borrego, and Justin Thon
# File name: project_main.py
# Date Created: 5/9/20
# Python version 3.7
# CST 205 - Multimedia Design & Programming
# Purpose: API call which returns detailed json about covid-19. Results
#		   are reprocessed into a local dictionary.
#

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