from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from PIL import Image
from states_coordinates import states_coordinates
from irregular_states import irregular_states
from states_names import states_names
from population_module import population
from covid_count import parsed_covid_data
from detailed_covid import DetailedCovidData
from borders import borders
from numpy import random as rnd
from state_to_abbrv import abbr
from imflip import meme_dictionary
from imflip import memes_list
import colorsys
import sys
import matplotlib
# import matplotlib.pyplot as plt
# import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np

matplotlib.use("TkAgg")
from matplotlib import pyplot as plt




def get_color_spread(N):
    HSV_tuples = [(x * 3.0 / N, 0.5, 0.5) for x in range(N)]
    hex_out = []
    for rgb in HSV_tuples:
        rgb = map(lambda x: int(x * 255), colorsys.hsv_to_rgb(*rgb))
        hex_out.append('#%02x%02x%02x' % tuple(rgb))
    return hex_out

states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA',
          'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD',
          'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ',
          'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC',
          'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']


## ------------------ color maker for all maps ----------------##

def linear_gradient(start_tuple, end_tuple, n):
    RGB_List = [start_tuple]

    hex_list = []

    for t in range(1, n):
        curr_vector = [
            int(start_tuple[j] + (float(t)/(n-1))*(end_tuple[j] - start_tuple[j]))
            for j in range(3)
        ]
        RGB_List.append(curr_vector)

    for i in range(len(RGB_List)):
        red = RGB_List[i][0]
        green = RGB_List[i][1]
        blue = RGB_List[i][2]
        color = (red, green, blue)
        converted_color = '#%02x%02x%02x' % color
        hex_list.append(converted_color)
    return hex_list
## ------------------- end color maker --------------------------##


## Population
sortPop = {k: v for k, v in sorted(population.items(), key=lambda x: x[1])}
states_pop_names_sorted = []

for value in sortPop:
    states_pop_names_sorted.append(value)
#print(states_pop_names_sorted)

colorgrade = linear_gradient((207,245,199), (2,77,5), 55)

color_pop = {}

for state, color in zip(states_pop_names_sorted, colorgrade):
    color_pop[state] = color

color_dictionary = color_pop
## End Population

## ------------------------------------------------------------------------------------- ##

## Cases
modCases = {}
for i in parsed_covid_data:
    modCases[i] = parsed_covid_data[i]['casesReported']
state_case_names = []
colorCase = linear_gradient((250,197,197), (101,2,2), 60)

#modCases.pop('Jurisdiction')

modCases = {k: v for k, v in sorted(modCases.items(), key=lambda x: x[1])}

for value in modCases:
    state_case_names.append(value)

color_cases = {}

for state, color in zip(state_case_names, colorCase):
    color_cases[state] = color

#print(state_case_names)

color_cases['borders'] = 'none'

## End Cases

## ------------------------------------------------------------------------------------- ##

## Recovered
modRecoveries = {}
for i in DetailedCovidData:
    modRecoveries[i] = DetailedCovidData[i]['recovered']

for i in modRecoveries:
    if(modRecoveries[i] == None):
        modRecoveries[i] = -1

modRecoveries = {k: v for k, v in sorted(modRecoveries.items(), key=lambda x: x[1])}

recv_state_names = []
colorRec = linear_gradient((118, 182, 241), (2, 45, 86), 60)

for value in modRecoveries:
    recv_state_names.append(value)

color_recovered = {}

for state, color in zip(recv_state_names, colorRec):
    if(modRecoveries[state] == -1):
        color_recovered[state] = '#f7bd72'
    else:
        color_recovered[state] = color

color_recovered['borders'] = 'none'
## End Recovered

## ------------------------------------------------------------------------------------- ##

## Deaths
modDeath = {}
for i in DetailedCovidData:
    modDeath[i] = DetailedCovidData[i]['death']

modDeath = {k: v for k, v in sorted(modDeath.items(), key=lambda x: x[1])}

death_state_names = []
colorDeath = linear_gradient((235, 199, 237), (147, 2, 116), 60)

for value in modDeath:
    death_state_names.append(value)

color_deaths = {}

for state, color in zip(death_state_names, colorDeath):
    color_deaths[state] = color

color_deaths['borders'] = 'none'

mystery_color = {}
mystery_color['borders'] = 'none'

#print(color_deaths)

## End Deaths

## ------------------------------------------------------------------------------------- ##
## Math Plot Lib Generator

def generatePlot(this_state_name, cases, recovered, deaths):
    objects = ('cases', 'recovered', 'deaths')
    y_pos = np.arange(len(objects))
    vals = [cases, recovered, deaths]

    plt.clf()

    plt.bar(y_pos, vals, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Persons')
    plt.title('State Statistics')

    plt.savefig("./static/images/" + this_state_name +".png")
    # plt.savefig("./static/images/plot.png")
    #plt.show()

## End Math Plot Lib
## ------------------------------------------------------------------------------------- ##

img_links = {}

for state in states_names:
    img_links[state] = ''

#print(img_links)

o30orMore = []
o25to30 = []
o20to25 = []
o15to20 = []
o10to15 = []
o5to10 = []

pdict = {
    "o30orMore" : [],
    "o25to30" : [],
    "o20to25" : [],
    "o15to20" : [],
    "o10to15" : [],
    "o5to10" : [],
    "o1to5" : [],
    "o900to1" : [],
    "o800to900" : [],
    "o700to800" : [],
    "o600to700" : [],
    "o500to600" : [],
    "under500" : []
}

color_dictionary['borders'] = 'none'


for state in population:
    if(population[state] > 5000000):
        if(population[state] > 30000000):
            #o30orMore.append(population[state])
            pdict['o30orMore'].append(state)
        elif(population[state] > 25000000 and population[state] < 30000000):
            # o25to30.append(population[state])
            pdict['o25to30'].append(state)
        elif(population[state] > 20000000 and population[state] < 25000000):
            # o20to25.append(population[state])
            pdict['o20to25'].append(state)
        elif(population[state] > 15000000 and population[state] < 20000000):
            # o15to20.append(population[state])
            pdict['o15to20'].append(state)
        elif(population[state] > 10000000 and population[state] < 15000000):
            # o10to15.append(population[state])
            pdict['o10to15'].append(state)
        elif(population[state] > 5000000 and population[state] < 10000000):
            # o5to10.append(population[state])
            pdict['o5to10'].append(state)
        #over.append(population[state])
    else:
        #under.append(population[state])
        #o5to10.append(state)
        if(population[state] > 1000000 and population[state] < 5000000):
            pdict['o1to5'].append(state)
        elif(population[state] > 900000 and population[state] < 1000000):
            pdict['o900to1'].append(state)
        elif(population[state] > 800000 and population[state] < 900000):
            pdict['o800to900'].append(state)
        elif(population[state] > 700000 and population[state] < 800000):
            pdict['o700to800'].append(state)
        elif(population[state] > 600000 and population[state] < 700000):
            pdict['o600to700'].append(state)
        elif(population[state] > 500000 and population[state] < 600000):
            pdict['o500to600'].append(state)
        else:
            pdict['under500'].append(state)
# for state in pdict:
#     print(state + " -> " + str(len(pdict[state])))

#print(pdict)

app = Flask(__name__)
app.secret_key = 'orthanc'
bootstrap = Bootstrap(app)

@app.route('/')
def home():
    #print(population)
    #print(borders)
        return render_template('home.html', title = "The R0na Tracker", states = states_coordinates, colors = color_dictionary, statesNames = states_names, borders = borders, irregstates = irregular_states, sorted_population = sortPop)

@app.route('/states/<state_id>')
def states_detail(state_id):
    #temp = color_dictionary['state_id']
    #print(DetailedCovidData[abbr[state_id]])

    local_dictionary = {'id' : state_id, 'population' : population[state_id], 'recovered' : DetailedCovidData[abbr[state_id]]['recovered'], 'death' : DetailedCovidData[abbr[state_id]]['death'], 'casesReported' : parsed_covid_data[state_id]['casesReported']}


    generatePlot(state_id, local_dictionary['casesReported'], modRecoveries[abbr[state_id]], local_dictionary['death'])

    return render_template('states_detail.html', state_info = local_dictionary, memes = memes_list)

@app.route('/covid_cases')
def covid_map():
    return render_template('covid_map.html', title = "The R0na Tracker", states = states_coordinates, colors = color_cases, statesNames = states_names, borders = borders, irregstates = irregular_states, sorted_population = modCases)

@app.route('/recoveries')
def recoveries():
    return render_template('recovery_map.html', title = "The R0na Tracker", states = states_coordinates, colors = color_recovered, statesNames = states_names, borders = borders, irregstates = irregular_states, sorted_population = modRecoveries)

@app.route('/deaths')
def deaths():
    return render_template('death_map.html', title = "The R0na Tracker", states = states_coordinates, colors = color_deaths, statesNames = states_names, borders = borders, irregstates = irregular_states, sorted_population = modDeath)

@app.route('/mysterymap')
def mysteries():
    print(img_links)
    return render_template('mystery_map.html', title = "The R0na Tracker", imgLink = img_links, states = states_coordinates, colors = mystery_color, statesNames = states_names, borders = borders, irregstates = irregular_states, sorted_population = sortPop)

@app.route('/mysterymapUpdate/<img_id>/<state_name_detail>')
def update(img_id, state_name_detail):
    print(img_id)
    print(state_name_detail)

    img_links[abbr[state_name_detail]] = meme_dictionary[img_id]['url']

    return mysteries()



if __name__ == '__main__':
    app.run(debug=True)
