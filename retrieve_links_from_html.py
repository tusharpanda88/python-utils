#coding:utf-8
import re

with open('Gaana.com.html','rb')as f:
	data = f.read()
	
data = data.replace('\r','').replace('\b','').replace('\n','')
find = re.compile(r'href="(.*?)"')
result = find.findall(data)
for x in result:
	if x.find("http") > -1:
		print x
