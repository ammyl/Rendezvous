#testing yweather

import yweather
client = yweather.Client()

new_york_id = client.fetch_woeid("Las Vegas, California") #tests for a string of a state
new_york_weather = client.fetch_weather(new_york_id)

print(new_york_weather)
