import re
import os

rxcountpages = re.compile(r"/Type\s*/Page([^s]|$)", re.MULTILINE|re.DOTALL)

def count_pages(filename):
    data = file(filename,"rb").read()
	print data
    return len(rxcountpages.findall(data))

if __name__=="__main__":
    filename = 'input.pdf'
    print count_pages(filename)
