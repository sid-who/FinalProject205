# FinalProject205
# The R0na Tracker

The R0na Tracker is a web based project that is intended to create awareness amongst all of the people of the United States. it shows you the number of infected people, the number of people who have died, and the recovered people. It takes the APIs and gets the Json information. This project creates tables and it is with a dynamic map, giving the user the ability to click each State and display every specific State's Statistics. Also, as a means of fun and as a means of entertaining people is quarantine days, this app comes with a really nice map that allows you to fill it out with memes. Memes come from another API, which displays the first 100 memes. This allows for a creative environment which can help us keep the user in our webpage for a while

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
python 3.7+ and the following libraries :

matplotlib

numpy

Flask

Flask-Bootstrap

requests

venv

numpy

urllib

json

requests
```

### Installing

A step by step series of examples that tell you how to get a development env running

Launch your virtual environment and then enter the following into command line to launch the flask app:

```
python3 project_main.py
```


End with an example of getting some data out of the system or using it for a little demo

## Running the tests

This web based project comes with a debugging mode by running python3 porject_main.py it will show if you have any problems with your code.

You will need flask to run this with the typical flask commands
```
FLASK_APP="project_main.py"
FLASK_DEBUG="1"
flask run
```

Alternatively, it can run via debug mode
```
python3 project_main.py
```

### Coding style tests

Our App intended to color code States according to the number of infected people. The Darker the color, the more infected people the State has. This at first was hard coded, which was good, but not as effective as we wanted. This was later replaced by a dictionary of colors, they are dynamically allocated and work with the density of the Population and density of COVID-19 cases.

```
## Case Sort - The following through "## End Cases"
## is used to sort our received dictionary from the API and arrange
## it according to ascending population information. Our gradient function
## is called and a color range is generated, the keys are then read into a
## new dictionary which is created by iterating through two lists. One being
## the state names arranged in the order the states appear in the dictionary,
## the other being the color gradient. zip() is used to accomplish this, and
## our new dictionary is built.
modCases = {}
for i in parsed_covid_data:
    modCases[i] = parsed_covid_data[i]['casesReported']
state_case_names = []
colorCase = linear_gradient((250,197,197), (101,2,2), 60)

#modCases.pop('Jurisdiction')
## The above may need to be commented in, depending on the updates to the API

modCases = {k: v for k, v in sorted(modCases.items(), key=lambda x: x[1])}

for value in modCases:
    state_case_names.append(value)

color_cases = {}

for state, color in zip(state_case_names, colorCase):
    color_cases[state] = color

color_cases['borders'] = 'none'
```

## Deployment

Local Flask application

## Built With

* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
* [Bootstrap](https://getbootstrap.com/)
* [Python](https://www.python.org/)
* [matplotlib](https://matplotlib.org/)


## Authors

Gurpreet Sidhu,
Jose Perez,
Cesar Borrego,
Justin Thon
https://github.com/sid-who/FinalProject205


## Acknowledgments

* [Color Gradients Tutorial](https://bsou.io/posts/color-gradients-with-python)

* [Covid-19 Cases API](https://api.apify.com/v2/key-value-stores/moxA3Q0aZh5LosewB/records/LATEST?disableRedirect=true)


* [Population API](https://datausa.io/api/data?drilldowns=State&measures=Population&year=latest)


* [ImgFlip API (Top 100)](https://api.imgflip.com/get_memes)


* [Covid Tracking API](https://covidtracking.com/api/states)
