import time
#current time
print "time  : ", time.asctime(time.localtime(time.time()))
#time since 1970
print time.time()
print "time : hour ", time.localtime(time.time())[3]
print "time : minute ", time.localtime(time.time())[4]
print "time : sec ", time.localtime(time.time())[5]
print time.clock()

import calendar
print calendar.month(2021,4)
