#prototype for app

import yweather
client = yweather.Client()
ID=client.fetch_woeid("New York City, New York")
    #input("Enter the your city followed by your state (Ex: Seattle, Washington):"))
Info=client.fetch_weather(ID)
Location = (Info["location"]["city"],Info["location"]["region"])
Temperature = (Info["condition"]["temp"])
Condition = (Info["condition"]["text"])
print(Location)
#Displays location name,and resion/state
print(Temperature)
#displays temperature of the city
print(Condition)
#prints textual version of weather condition (ex. cloudy, light rain)

