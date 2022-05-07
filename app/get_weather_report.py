import requests
def openweather():
    url= 'http://api.openweathermap.org/data/2.5/weather?q=Ljubljana&appid=8d3ef98ae6aefd864a88847b34a28f58&units=metric' 
    res = requests.get(url) 
    data = res.json() 
    #print("data: ", data)
    #copies data that we want from the dictonary
    temp = data['main']['feels_like']
    weather = data['weather'][0]['main']
    #print("temp: ", temp)
    #print("wreme: ", weather)
    weather_slo = weather_transaltion(weather)
    return temp, weather_slo

def weather_transaltion(x):
    y= 'nedefinirano vreme'
    if x == 'Thunderstorm':
        y = 'nevihta'
    elif x == 'Snow':
        y = 'sneg'
    elif x == 'Drizzle':
        y = 'rosi'
    elif x == 'Clear':
        y = 'jasno'
    elif x == 'Rain':
        y = 'dežuje'
    elif x == 'Wind':
        y = 'piha veter'
    elif x == 'Clouds':
        y = 'oblačno'
    #print("y: ", y)
    return y