from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from PIL import Image
from states_coordinates import states_coordinates
from states_names import states_names
from population_module import population
from covid_count import cases_by_state
from borders import borders
from numpy import random as rnd
import colorsys

def get_color_spread(N):
    HSV_tuples = [(x * 1.0 / N, 0.5, 0.5) for x in range(N)]
    hex_out = []
    for rgb in HSV_tuples:
        rgb = map(lambda x: int(x * 255), colorsys.hsv_to_rgb(*rgb))
        hex_out.append('#%02x%02x%02x' % tuple(rgb))
    return hex_out

colorgrade = get_color_spread(50)

# i = 0

states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

color_test = {}

for state, color in zip(states, colorgrade):
    color_test[state] = color

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


for state in population:
    if(population[state] > 5000000):
        if(population[state] > 30000000):
            #o30orMore.append(population[state])
            pdict['o30orMore'].append(population[state])
        elif(population[state] > 25000000 and population[state] < 30000000):
            # o25to30.append(population[state])
            pdict['o25to30'].append(population[state])
        elif(population[state] > 20000000 and population[state] < 25000000):
            # o20to25.append(population[state])
            pdict['o20to25'].append(population[state])
        elif(population[state] > 15000000 and population[state] < 20000000):
            # o15to20.append(population[state])
            pdict['o15to20'].append(population[state])
        elif(population[state] > 10000000 and population[state] < 15000000):
            # o10to15.append(population[state])
            pdict['o10to15'].append(population[state])
        elif(population[state] > 5000000 and population[state] < 10000000):
            # o5to10.append(population[state])
            pdict['o5to10'].append(population[state])
        #over.append(population[state])
    else:
        #under.append(population[state])
        #o5to10.append(state)
        if(population[state] > 1000000 and population[state] < 5000000):
            pdict['o1to5'].append(population[state])
        elif(population[state] > 900000 and population[state] < 1000000):
            pdict['o900to1'].append(population[state])
        elif(population[state] > 800000 and population[state] < 900000):
            pdict['o800to900'].append(population[state])
        elif(population[state] > 700000 and population[state] < 800000):
            pdict['o700to800'].append(population[state])
        elif(population[state] > 600000 and population[state] < 700000):
            pdict['o600to700'].append(population[state])
        elif(population[state] > 500000 and population[state] < 600000):
            pdict['o500to600'].append(population[state])
        else:
            pdict['under500'].append(population[state])
for state in pdict:
    print(state + " -> " + str(len(pdict[state])))


color_dictionary= {
    ##"AL" : "#FF5733"
        'AK': '#FF5733',
        'AL': '#7f3f3f',
        'AR': '#FF5733',
        'AZ': '#286ECE',
        'CA': '#FF5733',
        'CO': '#286ECE',
        'CT': '#FF5733',
        'DC': '#286ECE',
        'DE': '#FF5733',
        'FL': '#286ECE',
        'GA': '#FF5733',
        'GU': '#286ECE',
        'HI': '#FF5733',
        'IA': '#286ECE',
        'ID': '#FF5733',
        'IL': '#286ECE',
        'IN': '#FF5733',
        'KS': '#FF5733',
        'KY': '#286ECE',
        'LA': '#FF5733',
        'MA': '#286ECE',
        'MD': '#FF5733',
        'ME': '#286ECE',
        'MI': '#FF5733',
        'MN': '#286ECE',
        'MO': '#FF5733',
        'MS': '#286ECE',
        'MT': '#FF5733',
        'NA': '#FF5733',
        'NC': '#FF5733',
        'ND': '#FF5733',
        'NE': '#FF5733',
        'NH': '#FF5733',
        'NJ': '#FF5733',
        'NM': '#FF5733',
        'NV': '#FF5733',
        'NY': '#FF5733',
        'OH': '#FF5733',
        'OK': '#FF5733',
        'OR': '#FF5733',
        'PA': '#FF5733',
        'PR': '#FF5733',
        'RI': '#FF5733',
        'SC': '#FF5733',
        'SD': '#FF5733',
        'TN': '#FF5733',
        'TX': '#FF5733',
        'UT': '#FF5733',
        'VA': '#FF5733',
        'VI': '#FF5733',
        'VT': '#FF5733',
        'WA': '#FF5733',
        'WI': '#FF5733',
        'WV': '#FF5733',
        'WY': '#FF5733',
        'borders': 'none'

}



app = Flask(__name__)
app.secret_key = 'orthanc'
bootstrap = Bootstrap(app)

@app.route('/')
def home():
    #print(population)
    #print(borders)
    return render_template('home.html', states = states_coordinates, colors = color_dictionary, statesNames = states_names, borders = borders)

@app.route('/states/<state_id>')
def states_detail(state_id):
    #temp = color_dictionary['state_id']

    return render_template('states_detail.html', colors = color_dictionary)

if __name__ == '__main__':
    app.run(debug=True)
