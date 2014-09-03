
import urllib2
import urllib
import json
import pprint
url='http://api.ajaxsns.com/api.php?key=free&appid=0&msg='
while True:
	# strs=raw_input('u say:')

	strs='baidu.com'
	if strs=='fuck':
		break
	else:
		urls=url+strs
		response=urllib2.urlopen(urls)
		response=json.loads(response.read())
		print 'he say',response['content']
