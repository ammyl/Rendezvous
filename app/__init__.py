from flask import Flask, request, render_template, redirect, url_for
import sys
import os
from os import listdir
from os.path import isfile, join
import foursquare
import yweather
from geopy.geocoders import Nominatim
import random


app = Flask(__name__) 

clientWeather = yweather.Client()

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
    ID = clientWeather.fetch_woeid(city_state)
    Info = clientWeather.fetch_weather(ID)

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


    newLocation = str(latitude) + ", " + str(longitude)

    
    def determineOutIn(condition, temperature):
        if condition != "rainy" or temperature < 80 or temperature > 45:
            area = "outdoor"
        else:
            area = "indoor"
        return(area)
    determineOutIn(condition,temperature)

    area = determineOutIn(condition, temperature)
    
    
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
            result = outdoor(activity)
            return result

        elif area == "indoor":
            activity = random.choice(indoorList)
            result = indoor(activity)
            return result

        elif area == "night":
            activity = random.choice(nightList)
            result = nightLife(activity)
            return result

    def nameAndLocation(result):
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
        return[name, location]

    

    def string(area):
        
        #using this for the loop- 6 events: breakfast, 1st activity,
        #lunch, 2nd activity, dinner, and night activity
        i = 0
        while (i < 6):
            if i == 0:
                result = breakfast()
                list1 = nameAndLocation(result)
                
            elif i == 1:
                result = inOrOut(area)
                list2 = nameAndLocation(result)

            elif i == 2:
                result = lunch()
                list3 = nameAndLocation(result)
                
            elif i == 3:
                result = inOrOut(area)
                list4 = nameAndLocation(result)

            elif i == 4:
                result = dinner()
                list5 = nameAndLocation(result)

            elif i == 5:
                area = "night"
                result = inOrOut(area)
                list6 = nameAndLocation(result)
            
            i = i + 1
        
        returningList = [list1, list2, list3, list4, list5, list6]
        return(returningList)
    
    stuff = string(area)

    header = ["breakfast", "activity one", "lunch", "activity two", \
              "dinner", "activity three"]
    length = len(stuff)
    return render_template('schedule.html', city = city, \
                           temperature = temperature, \
                           condition = condition, stuff = stuff, \
                           header = header, length = length)








if __name__ == "__main__":
    app.run(debug=True)
