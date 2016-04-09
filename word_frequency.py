with open('test1.txt', 'r') as f:
    from collections import Counter
    c = Counter()
    for line in f:
        words = line.split()
        # print(words)
        c += Counter(words)
    for words in c.most_common():
    	print(words)
