from flask import Flask, request, render_template, redirect, url_for
import sys
import os
from os import listdir
from os.path import isfile, join
from clarify_python import clarify
import foursquare
from geopy.geocoders import Nominatim

app = Flask(__name__) 

# converting the obtained, raw data of an address into a string
def newAddress(address):
    anonAddress = ""
    for i in address:
        anonAddress = anonAddress + " " + i
    return(anonAddress)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('welcome.html')

@app.route('/tags', methods=['GET'])
def tags():
    
    client = foursquare.Foursquare(client_id='JEK02X44TGMNJSE0VC1UBEB4FRNNW3UMFQ4IQOPI4BAR2GXA', \
                                    client_secret='A2Z50VTUHHXEUYJBHCQKB1LXTNVVBYBQR4SDASVTXTWUMWXS') #foursquare shit

    address = request.args["address"] #address is currently a string
    geolocator = Nominatim()
    location = geolocator.geocode(address)
    newLocation = str(location.latitude) + str(", ") + str(location.longitude)


    return render_template('tags.html', newLocation = newLocation)


if __name__ == "__main__":
    app.run(debug=True)
