import re
f=open('./sinaweibo.py')
b=re.findall(r'http://w{3}.*com',f.read())
print b
f.close()
print f.read()
