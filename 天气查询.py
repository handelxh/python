# coding=utf-8
import urllib2
import urllib
import pprint
import json
url="http://api.thinkpage.cn/v2/weather"
values={"city":"beijing","language":"en","unit":"c","aqi":"city","key":"A70ZWYTRRT"}
data=urllib.urlencode(values)
# api="air.json"
# api="all.json"
api="suggestion.json"
theurl=url+"/"+api+"?"+data
response=urllib2.urlopen(theurl)
answer=json.loads(response.read())
# pprint.pprint(answer['weather'][0]['air_quality']['city'])
pprint.pprint(answer)
