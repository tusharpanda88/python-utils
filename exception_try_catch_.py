import os
fd1 = open("file1","r+")
while True:
	try:
		content = file.next(fd1)
	except StopIteration:
		print "EOF reached"
		break
	else:
		if content is None:
			print "EOF"
			break
		else:
			print content
	finally:
		print "exception or not, i will execute"

print "STOP"
fd1.close


###################################################################
import sys
try:
    sys.exit(0)
except SystemExit,err:
    print 'Tried to exit with code', err.code


###################################################################



