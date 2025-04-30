# You have a dictionary where each city has today's and yesterday's temperatures.
#
# Task:
#
# If today's temperature is higher than yesterday, create dictionary
# with key as city name and value as  "Getting Hotter", otherwise "Getting Cooler" or
# "Same" according to the condition.
#

city_weather = {
     'New York': {'today': 25, 'yesterday': 22},
     'Los Angeles': {'today': 30, 'yesterday': 32},
     'Chicago': {'today': 20, 'yesterday': 20},
     'Kochi':{'today':34,'yesterday':32}
}

new_dict = {}

for city, temp in city_weather.items():
    if temp['today'] > temp['yesterday']:
        new_dict[city] = "Getting Hotter"
    elif temp['today'] < temp['yesterday']:
        new_dict[city] = "Getting Cooler"
    else:
        new_dict[city] = "Same"

print(new_dict)