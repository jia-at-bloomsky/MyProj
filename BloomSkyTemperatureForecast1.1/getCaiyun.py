import requests
import urllib, json

def getCaiyun(LON,LAT,var): # 'temperature', 'humidity'
    url_forecast = "https://api.caiyunapp.com/v2/RQm8=v6xH=vVU12K/" + str(LON) + "," + str(
        LAT) + "/forecast.json?calback=MYCALLBACK?unit=metric:v2"
    response = urllib.urlopen(url_forecast)
    data_forecast = json.loads(response.read())
    data24 = []
    for ii in data_forecast[u'result'][u'hourly'][var]:
        data24.append(ii[u'value'])
    return data24[1:25]