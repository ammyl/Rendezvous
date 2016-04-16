import yweather

client = yweather.Client()
ID = client.fetch_woeid("Brooklyn, New York")
Info = (client.fetch_weather(ID))
print(Info[wind][chill])
print(Info[units][condition][temp])
print(Info[condition][image])
