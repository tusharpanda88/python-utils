import re
import operator

myfile = open('english_text.txt', 'r')
words = re.findall(r"[\w']+", myfile.read())
words_dictionary = {}

for word in words:
    if word not in words_dictionary:
        words_dictionary[word] = 0
        for item in words:
            if item == word:
                words_dictionary[word] += 1

sort_words_dictionary = sorted(words_dictionary.items(), key=operator.itemgetter(1), reverse=True)
print(sort_words_dictionary)
