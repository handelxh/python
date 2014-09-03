from weibo import APIClient
# import urllib2
import requests
APP_KEY = '4064761638' # app key
APP_SECRET = '37cd063f3dfa97746ead2385796f90f1' # app secret
# CALLBACK_URL = 'http://www.baidu.com' # callback url
CALLBACK_URL = 'http://www.baidu.com'
client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
url = client.get_authorize_url()
# print url
code = '17a3c16013c041d4c64361998cf7e9c9'
# code=raw_input('put the url to your browers,then get the code=')
r = client.request_access_token(code)
access_token = r.access_token
print access_token
expires_in = r.expires_in 
print expires_in
client.set_access_token(access_token, expires_in)
# print client.statuses.user_timeline.get()
# print client.statuses.update.post(status=u'test OAuth 2.0 send weibo to fuck the rip city, by LXH AT 2014/5/3')