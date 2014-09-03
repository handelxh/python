from douban_client import DoubanClient
import requests
API_KEY = '01674b2cf3fb7e9d0435e186dbf27bd7'
API_SECRET = '5fc3e181565091c7'
SCOPE = 'douban_basic_common,shuo_basic_r,shuo_basic_w'
your_redirect_uri = 'http://bbs.csdn.net/topics/370247707.com'
client = DoubanClient(API_KEY, API_SECRET, your_redirect_uri, SCOPE)
# print 'Go to the following link in your browser:'
print client.authorize_url
r = requests.post(client.authorize_url)
code = r.json()['code']
client.auth_with_code(110)
print client.user.me