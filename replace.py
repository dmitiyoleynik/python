
import re
import sys

f = open('/home/ubuntu/python/hello/hello/settings.py', 'r')

MyStr = f.read() 
f.close()

result = re.sub(r'{{{NAME}}}',sys.argv[1],MyStr)
result = re.sub(r'{{{USER}}}',sys.argv[2],result)
result = re.sub(r'{{{PASS}}}',sys.argv[3],result)
result = re.sub(r'{{{HOST}}}',sys.argv[4],result)

f = open('/home/ubuntu/python/hello/hello/settings.py', 'w')
f.write(result)




