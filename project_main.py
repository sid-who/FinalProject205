from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from PIL import Image
from states_coordinates import states_coordinates
from states_names import states_names
from population_module import population
from covid_count import cases_by_state
from borders import borders

color_dictionary= {
    ##"AL" : "#FF5733"
        'AK': '#FF5733',
        'AL': '#286ECE',
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
    print(borders)
    return render_template('home.html', states = states_coordinates, colors = color_dictionary, statesNames = states_names, borders = borders)

@app.route('/states/<state_id>')
def states_detail(state_id):
    #temp = color_dictionary['state_id']

    return render_template('states_detail.html', colors = color_dictionary)

if __name__ == '__main__':
    app.run(debug=True)
