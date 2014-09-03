import urllib2
import urllib
import pprint
import json
import chardet
url = "http://api.map.baidu.com/location/ip"
values = {"ip": "211.71.92.202", "ak":
          "9L9g136CBV2bY9lBPMZeTLVU", "coor": "bd09ll"}
data = urllib.urlencode(values)
# print data
theurl = url + "?" + data
# print theurl
response = urllib2.urlopen(theurl)
answer = response.read()
# answer=json.loads(answer,encoding="gbk")
# pprint.pprint(answer)
print answer
