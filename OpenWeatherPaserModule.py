#-*-coding:utf-8

from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus
import json
import time
import ast

def APIParse(service_key, cityid, doc): #요청을 보내고 결과를 받는 함수
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

    return weather, avertemp,temp, humidity, pressure

def excute(run, key, city):#파서 함수를 실행
    find = True
    count = 0

    with open('city.list.kr.json') as citylistjson:
        #with문은 도시 목록을 불러옴
        #한국 도시 리스트만 불러옵니다.
        citylist = json.load(citylistjson)
        citylist = ast.literal_eval(str(citylist))

        while find == True:
            #입력받은 도시의 코드 찾기
            tmp = citylist[count]
            if tmp["name"] == city:
                print(tmp.get("_id"))
                find = False
                #찾으면 반복문 종료
            count += 1

    while run == True:
        data = APIParse(key, '1835847', False)
        print(data)
        time.sleep(1800)
        #30분에 한번씩 요청을 보낸다.

#예시 요청
excute(True, "e439f48431e739fcfd6c3127c1d0d582", <CITY>)

'''
excute함수에서 APIParse를 호풀해서 사용한다
 이그제큐트만 호출해서 사용하세요.
'''
