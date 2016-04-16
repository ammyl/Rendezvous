from flask import Flask, request, render_template, redirect, url_for
import sys
import os
from os import listdir
from os.path import isfile, join
import foursquare

app = Flask(__name__) 

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('welcome.html')

@app.route('/tags', methods=['GET'])
def tags():
    
    client = foursquare.Foursquare(client_id='JEK02X44TGMNJSE0VC1UBEB4FRNNW3UMFQ4IQOPI4BAR2GXA', \
                                    client_secret='A2Z50VTUHHXEUYJBHCQKB1LXTNVVBYBQR4SDASVTXTWUMWXS') #foursquare shit

    zipcode = request.args["zipcode"]
    

    return render_template('schedule.html')


if __name__ == "__main__":
    app.run(debug=True)
