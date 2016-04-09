import os
import re

# set diaries path
diaries_path = "diaries/"
diaries = os.listdir(diaries_path)

# set stop words to make informative keywords
stop_words = open("StopWords.txt", 'r').read()
stop_words_list = stop_words.split(" ")


# Find top 5 keywords in a txt
def find_keywords(words):
    words_dictionary = {}
    for word in words:
        if word.lower() not in words_dictionary and word.lower() not in stop_words_list:
            # Put word in dictionary
            words_dictionary[word] = 0
            for item in words:
                if item == word:
                    words_dictionary[word] += 1
    # Find 5 keywords which by highest frequency
    keywords = sorted(
        words_dictionary, key=words_dictionary.__getitem__, reverse=True)[0:5]
    return keywords

for diary in diaries:
    # Coding by utf-8
    with open(diaries_path + diary, "r") as content:
        diary_words_list = re.findall(r"[\w']+", content.read())
        print("The keywords of diary " + diary + " is: ")
        print(find_keywords(diary_words_list))
