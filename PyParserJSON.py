#OpenAPI
'''
                                                                                                                                                                                                        import xml.etree.ElementTree as ET
import urllib.request
from xml.etree.ElementTree import parse

def subper(sub) :
    url = "http://data.jeju.go.kr/rest/JejuLdapsDataService/getForecastPointDataXY"

    tree = ET.ElementTree(file=urllib.request.urlopen(url))
    root = tree.getroot()

    return root

print(subper("nx"))
'''
import json
from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus
url = 'http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastGrib'
service_key = 'NgWWeOgssOHILkuc0IgP9n93E9fBCOAftdEqhYEibSDKxGH0oIff49VSTkYiNh1hFaEpQbt4%2BvRhSAW3mANIKw%3D%3D'
Now_date = 20170329
Now_time = '0600'
nx = 60
ny = 157


queryParams = '?' + urlencode({quote_plus('ServiceKey') : service_key},{quote_plus('base_date') : Now_date, quote_plus('base_time') : Now_time, quote_plus('NX') : nx, quote_plus('NY') : ny,quote_plus('numOfRows') : 10,quote_plus('pageNO') : 1,quote_plus('_type') : 'json'})

request = Request(url + queryParams)
request.get_method = lambda: 'GET'
response_body = urlopen(request).read()

print(response_body)




