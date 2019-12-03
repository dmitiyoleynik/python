
import re
import sys

f = open('/home/ubuntu/python/hello/hello/settings.py', 'r')

MyStr = f.read() 
f.close()

result = re.sub(r'{{{NAME}}}',sys.argv[1],MyStr)
result = re.sub(r'{{{USER}}}',sys.argv[2],MyStr)
result = re.sub(r'{{{PASS}}}',sys.argv[3],MyStr)
result = re.sub(r'{{{HOST}}}',sys.argv[4],MyStr)

f = open('/home/ubuntu/python/hello/hello/settings.py', 'a')
f.write(MyStr)




