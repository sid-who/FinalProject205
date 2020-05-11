#
# Code by Gurpreet Sidhu, Jose Perez, Cesar Borrego, and Justin Thon
# File name: project_main.py
# Date Created: 5/9/20
# Python version 3.7
# CST 205 - Multimedia Design & Programming
# Purpose: Flask application which is dependent several modules performing api calls. This
#          application displays several renderings of an svg map with fills according to 
#          population, covid-case, recovery, and death density. This occurs at a state 
#          level, Flask and jinja are used to create dynamic routes to each state on each page.
#          At the state level, smaller details are displayed. A meme can be selected from the
#          the gallery and it will be applied to that state on the '???' tab
#



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
import numpy as np

matplotlib.use("TkAgg")
from matplotlib import pyplot as plt

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

## End Math Plot Lib
## ------------------------------------------------------------------------------------- ##

img_links = {}

for state in states_names:
    img_links[state] = ''

color_dictionary['borders'] = 'none'

app = Flask(__name__)
app.secret_key = 'orthanc'
bootstrap = Bootstrap(app)

@app.route('/')
def home():
        return render_template('home.html', title = "The R0na Tracker", states = states_coordinates, colors = color_dictionary, statesNames = states_names, borders = borders, irregstates = irregular_states, sorted_population = sortPop)

@app.route('/states/<state_id>')
def states_detail(state_id):
    local_dictionary = {'id' : state_id, 'population' : population[state_id], 'recovered' : DetailedCovidData[abbr[state_id]]['recovered'], 'death' : DetailedCovidData[abbr[state_id]]['death'], 'casesReported' : parsed_covid_data[state_id]['casesReported']}


    generatePlot(state_id, local_dictionary['casesReported'], modRecoveries[abbr[state_id]], local_dictionary['death'])

    percent_infected = (parsed_covid_data[state_id]['casesReported']/population[state_id])

    percentage = "{:.001%}".format(percent_infected)

    return render_template('states_detail.html', state_info = local_dictionary, memes = memes_list, percent = percentage)

@app.route('/covid_cases')
def covid_map():
    return render_template('covid_map.html', title = "The R0na Tracker", states = states_coordinates, colors = color_cases, statesNames = states_names, borders = borders, irregstates = irregular_states, sorted_population = modCases)

@app.route('/recoveries')
def recoveries():
    return render_template('recovery_map.html', title = "The R0na Tracker", states = states_coordinates, colors = color_recovered, statesNames = states_names, borders = borders, irregstates = irregular_states, sorted_population = modRecoveries, abbreviations = abbr)

@app.route('/deaths')
def deaths():
    return render_template('death_map.html', title = "The R0na Tracker", states = states_coordinates, colors = color_deaths, statesNames = states_names, borders = borders, irregstates = irregular_states, sorted_population = modDeath, abbreviations = abbr)

@app.route('/mysterymap')
def mysteries():
    print(img_links)
    return render_template('mystery_map.html', title = "The R0na Tracker", imgLink = img_links, states = states_coordinates, colors = mystery_color, statesNames = states_names, borders = borders, irregstates = irregular_states, sorted_population = sortPop)

@app.route('/mysterymapUpdate/<img_id>/<state_name_detail>')
def update(img_id, state_name_detail):
    img_links[abbr[state_name_detail]] = meme_dictionary[img_id]['url']

    return mysteries()



if __name__ == '__main__':
    app.run(debug=True)
