# doding:utf-8
# import win32api
# import win32con
# print help(win32api)
# win32api.MessageBox(win32con.NULL, 'hello', 'python', win32con.MB_OK)
import chardet
import urllib2
import re
# print help(chardet)
# print chardet.detect(response)['encoding']
response=urllib2.urlopen('http://baidu.com')
# print response.read()
response=response.read()
# response=str(response)
print response
ha=re.findall('[a-zA-z]+://[^\s]*/',response)
print ha[0]
# print ha.group()
