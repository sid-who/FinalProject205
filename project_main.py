from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from PIL import Image
from states_coordinates import states_coordinates
from irregular_states import irregular_states
from states_names import states_names
from population_module import population
from covid_count import cases_by_state
from borders import borders
from numpy import random as rnd
import colorsys

from flask_nav import Nav
from flask_nav.elements import Navbar, View


def get_color_spread(N):
    HSV_tuples = [(x * 3.0 / N, 0.5, 0.5) for x in range(N)]
    hex_out = []
    for rgb in HSV_tuples:
        rgb = map(lambda x: int(x * 255), colorsys.hsv_to_rgb(*rgb))
        hex_out.append('#%02x%02x%02x' % tuple(rgb))
    return hex_out

#colorgrade = get_color_spread(100)

# i = 0

states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 
          'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 
          'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 
          'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 
          'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']

# color_test = {}

# for state, color in zip(states, colorgrade):
#     color_test[state] = color

#color_dictionary = color_test

sortPop = {k: v for k, v in sorted(population.items(), key=lambda x: x[1])}

print(sortPop)

states_pop_names_sorted = []

for value in sortPop:
    #print(value + " - " + str(sortPop[value]))
    states_pop_names_sorted.append(value)
print(states_pop_names_sorted)


## ------------------ color maker for population map ----------------##

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

colorgrade = linear_gradient((207,245,199), (2,77,5), 55)

color_pop = {}

for state, color in zip(states_pop_names_sorted, colorgrade):
    color_pop[state] = color

color_dictionary = color_pop



#color_dictionary = linear_gradient((207,245,199), (22,89,9), 60)



# print(color_test)

# print(sorted(population.values()))

# print(population)

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
for state in pdict:
    print(state + " -> " + str(len(pdict[state])))

#print(pdict)

app = Flask(__name__)
app.secret_key = 'orthanc'
bootstrap = Bootstrap(app)

@app.route('/')
def home():
    #print(population)
    #print(borders)
    return render_template('home.html', states = states_coordinates, colors = color_dictionary, statesNames = states_names, borders = borders, irregstates = irregular_states)

@app.route('/states/<state_id>')
def states_detail(state_id):
    #temp = color_dictionary['state_id']

    return render_template('states_detail.html', colors = color_dictionary)

@app.route('/covid_cases')
def covid_map():
    return render_template('covid_map.html')

@app.route('/recoveries')
def recoveries():
    return render_template('recovery_map.html')

@app.route('/deaths')
def deaths():
    return render_template('death_map.html')

@app.route('/mysterymap')
def mysteries():
    return render_template('mystery_map.html')


if __name__ == '__main__':
    app.run(debug=True)
