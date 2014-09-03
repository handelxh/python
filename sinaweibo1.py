# -*- coding:utf-8 -*-
from weibo import APIClient
APP_KEY = '4064761638' # app key
APP_SECRET = '37cd063f3dfa97746ead2385796f90f1' # app secret
# CALLBACK_URL = 'http://www.baidu.com' # callback url
CALLBACK_URL = 'http://www.baidu.com'
client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
access_token = '2.00SrYGlBaL1F8Eb7677005a1UoPQ2E'
# print access_token
expires_in = '1556811461' 
# print expires_in
client.set_access_token(access_token, expires_in)
# print client.statuses.user_timeline.get()
# print client.statuses.update.post(status=u'test OAuth 2.0 send weibo to fuck the rip city, by LXH AT 2014/5/3')
import requests
import  json
pram={'source':'4064761638','access_token':'2.00SrYGlBaL1F8Eb7677005a1UoPQ2E','ip':'124.207.38.202'}
r=requests.get('https://api.weibo.com/2/location/geo/ip_to_geo.json',params=pram)
r=r.json()
import pprint 
pprint.pprint(r)

