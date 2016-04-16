from flask import Flask, request, render_template, redirect, url_for
import sys
import os
from os import listdir
from os.path import isfile, join
import foursquare
import yweather

app = Flask(__name__) 

client = yweather.Client()

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('welcome.html')

@app.route('/schedule', methods=['GET'])
def schedule():
    
  #  client = foursquare.Foursquare(client_id='JEK02X44TGMNJSE0VC1UBEB4FRNNW3UMFQ4IQOPI4BAR2GXA', \
   #                                 client_secret='A2Z50VTUHHXEUYJBHCQKB1LXTNVVBYBQR4SDASVTXTWUMWXS') #foursquare shit

    city_state = request.args["city_state"] # New York City, New York

    # weather part
    ID = client.fetch_woeid(city_state)
    Info = client.fetch_weather(ID)

    # info gotta pass
    location = (Info["location"]["city"],Info["location"]["region"])
    temperature = (Info["condition"]["temp"])
    condition = (Info["condition"]["text"])

    return render_template('schedule.html', location = location, \
                           temperature = temperature, \
                           condition = condition)


if __name__ == "__main__":
    app.run(debug=True)
