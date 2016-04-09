import os,re
from collections import Counter
import nltk
from nltk.corpus import stopwords

useless_words=['the','I','and','']
def main():
	for file in os.listdir("."):
		result=Counter()
		if file.endswith('.text'):
			with open(file,'rt') as f:
				for line in f:
					# delete the stopwords in note
					words=line.split()
					words= [w for w in words if not w in stopwords.words('english')]
					result+=Counter(words)
			print('The most important word in %s is %s',(file,result.most_common(2)))

if __name__ == '__main__':
	main()
