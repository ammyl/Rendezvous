from flask import Flask, request, render_template, redirect, url_for
import sys
import os
from os import listdir
from os.path import isfile, join
import foursquare
import yweather
from geopy.geocoders import Nominatim


app = Flask(__name__) 

client = yweather.Client()

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('welcome.html')

@app.route('/schedule', methods=['GET'])
def schedule():

    #foursquare shit
    client = foursquare.Foursquare(client_id='JEK02X44TGMNJSE0VC1UBEB4FRNNW3UMFQ4IQOPI4BAR2GXA', \
                                    client_secret='A2Z50VTUHHXEUYJBHCQKB1LXTNVVBYBQR4SDASVTXTWUMWXS') 

    city_state = request.args["city_state"] # New York City, New York

    # weather part
    ID = client.fetch_woeid(city_state)
    Info = client.fetch_weather(ID)

    # info gotta pass
    location = (Info["location"]["city"],Info["location"]["region"])
    temperature = (Info["condition"]["temp"])
    condition = (Info["condition"]["text"]).lower()
    
    city = str(location[0]) + ", " + str(location[1])

    city2 = str(location[0]) + " " + str(location[1])
    # activities part

    
    outdoorList = ["rock climbing", "park", "tennis court", "barbecue",
               "swimming pool", "running", "amusement park"]

    indoorList = ["indoor rock climbing", "bowling", "museum", "art museum",
              "indoor ice skating", "shopping", "pool", "spa", "library",
              "movie", "theater"]
              
    nightList = ["bar", "nightlife", "movie", "bowling"]
    
    geolocator = Nominatim()
    city = geolocator.geocode(city2)
    latitude = city.latitude
    longitude = city.longitude


    coordinates = str(latitude) + ", " + str(longitude)

    if condition != "rainy" or temperature > 80 or temperature < 45:
        area = "outdoor"
    else:
        area = "indoor"

    inOrOut(area)

    
    
    return render_template('schedule.html', city = city, \
                           temperature = temperature, \
                           condition = condition)

def indoor(activity):
    return (client.venues.search(params={'ll': newLocation, 
                                         'query': activity}))

def outdoor(activity):
    return(client.venues.search(params={'ll': newLocation, 
                                        'query': activity}))

def breakfast():
    return(client.venues.search(params={'ll': newLocation, 
                                        'query': "breakfast"}))

def lunch():
    return(client.venues.search(params={'ll': newLocation, 
                                        'query': "lunch"}))

def dinner():
    return(client.venues.search(params={'ll': newLocation, 
                                        'query': "dinner"}))

def nightLife(activity):
    return(client.venues.search(params={'ll': newLocation, 
                                        'query': activity}))

def inOrOut(area):
    if area == "outdoor":
        activity = random.choice(outdoorList)
        print (activity)
        result = outdoor(activity)
        return result

    elif area == "indoor":
        activity = random.choice(indoorList)
        print (activity)
        result = indoor(activity)
        return result

    elif area == "night":
        activity = random.choice(nightList)
        print(activity)
        result = nightLife(activity)
        return result

def nameAndLocation(result, string):
    for x in result:
        #this is the one big definition to the one key
        key = (result[x])
        #this picks a random number
        which = random.randint(0,len(key)-1)
        #picks a venue from the random number
        venue = key[which]
        #looks through venue attributes to find name and location
        for key in venue:
            if key == "location":
                locationDict = venue[key]
                for lkey in locationDict:
                    if lkey == "address":
                        location = locationDict[lkey]
                    elif lkey == "formattedAddress":
                        location = locationDict[lkey]
                        
            if key == "name":
                name = venue[key]
        string = string + " Name: " + name + "\n" + "Location" + location + "\n"


def main():
    string = ""
    
    #using this for the loop- 6 events: breakfast, 1st activity,
    #lunch, 2nd activity, dinner, and night activity
    i = 0
    while (i < 6):
        if i == 0:
            print("breakfast")
            result = breakfast()
            nameAndLocation(result, string)
            
        elif i == 1:
            print("after breakfast activity")
            result = inOrOut(area)
            nameAndLocation(result, string)

        elif i == 2:
            print("lunch")
            result = lunch()
            nameAndLocation(result, string)
            
        elif i == 3:
            print("after lunch activity")
            result = inOrOut(area)
            nameAndLocation(result, string)

        elif i == 4:
            print("dinner")
            result = dinner()
            nameAndLocation(result, string)

        elif i == 5:
            area = "night"
            print("after dinner activity")
            result = inOrOut(area)
            nameAndLocation(result, string)
        
        i = i + 1
        



if __name__ == "__main__":
    app.run(debug=True)
