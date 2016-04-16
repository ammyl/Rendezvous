#Flawless Hacks 04/16/2016 Ammy Lin | Ellie Ly | Michelle Lam

import foursquare
import random

client = foursquare.Foursquare(client_id='JEK02X44TGMNJSE0VC1UBEB4FRNNW3UMFQ4IQOPI4BAR2GXA', client_secret='A2Z50VTUHHXEUYJBHCQKB1LXTNVVBYBQR4SDASVTXTWUMWXS')

#lists of activities
outdoorList = ["rock climbing", "park", "tennis court", "barbecue",
               "swimming pool", "running", "amusement park"]

indoorList = ["indoor rock climbing", "bowling", "museum", "art museum",
              "indoor ice skating", "shopping", "pool", "spa", "library",
              "movie", "theater"]
              
nightList = ["bar", "nightlife", "movie", "bowling"]

#remember this is temporary - need to get location of city/state and turn it
#into newLocation as coordinates
newLocation = "40.71405, -74.00594"

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
        print ("Name:", name)
        print("Location:", location)


def main():
    #this is temporary - need to get this from weather
    area = "outdoor"
    
    #using this for the loop- 5 events: breakfast, 1st activity,
    #lunch, 2nd activity, dinner, and night activity
    i = 0
    while (i < 6):
        if i == 0:
            print("breakfast")
            result = breakfast()
            nameAndLocation(result)
            
        elif i == 1:
            print("after breakfast activity")
            result = inOrOut(area)
            nameAndLocation(result)

        elif i == 2:
            print("lunch")
            result = lunch()
            nameAndLocation(result)
            
        elif i == 3:
            print("after lunch activity")
            result = inOrOut(area)
            nameAndLocation(result)

        elif i == 4:
            print("dinner")
            result = dinner()
            nameAndLocation(result)

        elif i == 5:
            area = "night"
            print("after dinner activity")
            result = inOrOut(area)
            nameAndLocation(result)
        
        i = i + 1


        
main()










