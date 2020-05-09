import requests
import urllib
import json

URL = "https://datausa.io/api/data?drilldowns=State&measures=Population&year=latest"

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

requests = requests.get(url = URL, headers=headers)

pop_dict = requests.json()

#print(pop_dict['data'][0]['State'])

#print(pop_dict)

population = {}

for i in range(len(pop_dict['data'])):
	state_name = pop_dict['data'][i]['State']
	population_number = pop_dict['data'][i]['Population']
	population[state_name] = population_number

#print(population)

print(population)

