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
        'AL': '#FF5733',
        'AR': '#FF5733',
        'AZ': '#FF5733',
        'CA': '#FF5733',
        'CO': '#FF5733',
        'CT': '#FF5733',
        'DC': '#FF5733',
        'DE': '#FF5733',
        'FL': '#FF5733',
        'GA': '#FF5733',
        'GU': '#FF5733',
        'HI': '#FF5733',
        'IA': '#FF5733',
        'ID': '#FF5733',
        'IL': '#FF5733',
        'IN': '#FF5733',
        'KS': '#FF5733',
        'KY': '#FF5733',
        'LA': '#FF5733',
        'MA': '#FF5733',
        'MD': '#FF5733',
        'ME': '#FF5733',
        'MI': '#FF5733',
        'MN': '#FF5733',
        'MO': '#FF5733',
        'MS': '#FF5733',
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
    print(population)
    return render_template('home.html', states = states_coordinates, colors = color_dictionary, statesNames = states_names, borders = borders)

@app.route('/states/<state_id>')
def states_detail(state_id):
    #temp = color_dictionary['state_id']

    return render_template('states_detail.html', colors = color_dictionary)

if __name__ == '__main__':
    app.run(debug=True)
