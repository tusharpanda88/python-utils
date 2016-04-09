#if statement
#Write a function that includes each of the following:

#    An if statement with an elif clause and an else clause.
#    Write several if statements that use the logical operators: and, or, and not. Or, maybe a single if statement that uses them all.
#    Use the range() built-in function to create a list, for example: numbers = range(10). Write an if statement that tests a value to determine if it is in a list.
#    Write an if statement that tests whether the value is not in the list (above).
#    Create a small dictionary, for example: fruit = {'watermelon': 44}. Write an if statement that tests whether a key is in the dictionary and tests whether the value (associated with that key) is equal to some value (such as 44).
#    Assign a value to a variable, then write an if statement to determine whether that value is the same as None and another if statement to test whether the value is not None.



#
# if statement
#
def test_if():
    list1 = ['apple', 'banana', 'cherry', 'date', ]
    for item in list1:
        if item == 'apple':
            print "it's an apple"
        elif item == 'banana':
            print "it's a banana"
        elif item == 'cherry':
            print "it's a cherry"
        else:
            print "it's an other --", item
    v1 = 3
    v2 = 5
    v3 = 7
    if not (v1 < v2 and v2 < v3) or v1 != v2:
        print 'yes'
    else:
        print 'no'
    list2 = range(10)
    value1 = 5
    value2 = 20
    if value1 in list2:
        print "it's in -- %d" % value1
    if value2 not in list2:
        print "it's not -- %d" % value2
    dict1 = {'watermelon': 4}
    key1 = 'watermelon'
    if key1 in dict1 and dict1[key1] == 4:
        print "it's good"
    key2 = 'cantaloupe'
    if key2 in dict1 and dict1[key2] == 4:
        print "it's bad"
