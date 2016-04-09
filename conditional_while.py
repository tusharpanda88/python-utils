#Qns:
# Use a while statement to loop through a list of words and to find the first word with a specific number of characters.
# Use a while statement to loop through a list; pop each item off the right end of the list and print the item, until the list is empty.
# Write a function that uses a while statement and str.find(pat, pos) to print out all the positions of a pattern string in a target string.
# Convert the above function into a function that returns a generator that produces all the positions of the pattern string in a target string.




#
# while statement
#
def test_while(word_length):
    words = ['a', 'bb', 'ccc', 'dddd', ]
    idx = 0
    word = None
    while idx < len(words):
        if len(words[idx]) == word_length:
            word = words[idx]
            break
        idx += 1
    print 'word: "%s"' % word
    print '-' * 20
    word_length += 20
    while idx < len(words):
        if len(words[idx]) == word_length:
            word = words[idx]
            break
        idx += 1
    else:
        word = None
    print 'word: "%s"' % word
    print '-' * 20
    items = range(10, 14)
    while items:
        item = items.pop()
        print 'popped item:', item
    return word


def search_positions(pat, target):
    pos = 0
    while True:
        pos = target.find(pat, pos)
        if pos < 0:
            break
        print 'search pos:', pos
        pos += 1


def generate_positions(pat, target):
    pos = 0
    while True:
        pos = target.find(pat, pos)
        if pos < 0:
            break
        yield pos
        pos += 1


def apply_at_positions(pat, target, func):
    pos = 0
    while True:
        pos = target.find(pat, pos)
        if pos < 0:
            break
        func(pos, target[pos:pos + len(pat)])
        pos += 1


def func1(pos, str_val):
    print 'apply at pos: %d  "%s"' % (pos, str_val.upper(), )


