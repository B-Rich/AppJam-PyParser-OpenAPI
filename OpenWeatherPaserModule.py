from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus
import json
import time

def APIParse(service_key, cityid, doc, run):
    if doc == True:
        print('''APIParse(KEY, ID, DOC-TRUE-FALSE, RUN-TRUE-FALSE)''')
    url = 'http://api.openweathermap.org/data/2.5/weather'

    queryParams = '?' + urlencode({quote_plus('id'): cityid}) + '&' + urlencode({quote_plus('APPID'): service_key})
    request = Request(url + queryParams)
    request.get_method = lambda: 'GET'
    response_body = (urlopen(request).read()).decode("utf-8")

    WeatherData = json.loads(response_body)

    weather = WeatherData['weather'][0]
    weather = weather['main']

    temp_min = WeatherData['main']['temp_min'] - 273.15
    temp_max = WeatherData['main']['temp_max'] - 273.15
    avertemp = (temp_max + temp_min) / 2

    humidity = WeatherData['main']['humidity']

    pressure = WeatherData['main']['pressure']

    temp = WeatherData['main']['temp'] - 273.15

    return weather, avertemp,temp, humidity, pressure, time.time()

def excute(run):
    while run == True:
        data = APIParse('de82d6d4bc81413bce54f58ec194befb', '1835847', True, True)
        print(data)
        time.sleep(1800)

excute(True)
print(APIParse('de82d6d4bc81413bce54f58ec194befb', '1835847', True, True))
