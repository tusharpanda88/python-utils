#!/usr/bin/env python3

import re
import requests

r = requests.get('https://github.com')
print type(r)
matches = re.findall('(?:https?|ftp)://[^\s/$\.?#].[^\s]+', r.text)

for i in range(0, len(matches)):
    print('matche >>>: {} \n'.format(matches[i]))
