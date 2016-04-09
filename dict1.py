#!/usr/bin/env
'''
the following code is a  preliminary word processing, 
it won't split abbrevations, like "I'd", nor it won't split words
concatenated with underscore, like "bad_game"
'''
import os
import re
def word_count(file_path):
	word_dict = {}
	with open(file_path) as txt:
		for line in txt:
			words = re.findall(r"\w+", line.strip()) 
			for word in words:
				word = word.lower()
				word_dict[word] = word_dict.get(word,0) + 1
	return word_dict

result = word_count(os.path.join(os.path.dirname(os.path.abspath(__file__)), "sampletext.txt"))

###################################################################################

'''
"How to "sort" a dict by its key/value"
Obviously, a dict can not be sorted, since it is orderless in nature.
However, what we can do is to sort a representation(a list of tuples or a list of keys) of dict. 
link: http://stackoverflow.com/questions/613183/sort-a-python-dictionary-by-value
'''

import operator
d = {"what": 3, "I": 19, "the":30}
# to get a list of tuples with sorted items by the value
sorted_d_by_value = sorted(d.items(), key=operator.itemgetter(1))
# to get a list of tuples with sorted key
sorted_d_by_key = sorted(d.items(), key=operator.itemgetter(0))
print sorted_d_by_key



