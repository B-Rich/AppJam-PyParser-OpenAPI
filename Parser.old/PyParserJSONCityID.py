#-*-coding:utf-8

from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus
import json
url = 'http://api.openweathermap.org/data/2.5/weather'
service_key = 'de82d6d4bc81413bce54f58ec194befb'
cityid = '1835847' #seoul

queryParams = '?' + urlencode({quote_plus('id') : cityid}) + '&' + urlencode({quote_plus('APPID') : service_key})
request = Request(url + queryParams)
request.get_method = lambda: 'GET'
response_body = urlopen(request).read()


response_body = response_body.decode('utf-8')

f = open("APIdata.json", 'w')
f.write(response_body)

WeatherData = json.loads(response_body)

weather = WeatherData['weather'][0]
weather = weather['main']

temp_min = WeatherData['main']['temp_min'] - 273.15
temp_max = WeatherData['main']['temp_max'] - 273.15
avertemp = (temp_max + temp_min) / 2

humidity = WeatherData['main']['humidity']

pressure = WeatherData['main']['pressure']

temp = WeatherData['main']['temp'] - 273.15

print(weather, avertemp, temp, humidity, pressure)

f.close()