#testing yweather

import yweather
client = yweather.Client()

# user inputs the location; return the weather info

# problem, figure out how to test for a zip code
new_york_id = client.fetch_woeid("New York, USA") #tests for a string of a state
new_york_weather = client.fetch_weather(new_york_id)

print(new_york_weather)
