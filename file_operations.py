
#open-close check
fd = open("file1","r+")
print "name 	",fd.name
print "closed 	",fd.closed
fd.close()
print "closed 	",fd.closed

#append
fd = open("file1","a+")
fd.write("cassidy");
fd.close()

#read file1 & write to file2
fd1 = open("file1","a+")
fd2 = open("file2","r")
content2 = fd2.read();
fd1.write(content2);
fd1.close()
fd2.close()

#cursor position
fd1 = open("file1","r+")
position = fd1.tell()
print position
position = fd1.seek(4,0)
print position
content = fd1.read()
print content
fd1.close()


#read file line by line
with open("symbols",'rb') as f:
    while True:
        line=f.readline()   ##f.readline(5) read 5 lines
        if not line: break
        process(line)




######file operations----------------------------------
import os
os.rmdir("dir1")
os.mkdir("dir1")
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

#------------------------------------------------------

##############################################################################

with open('file1') as f:
	lines = f.readlines()
	line = lines.rstrip('\n')
	print line

#lines = [line.rstrip('') for line in open('file1')]
#lines = [line.strip('\t').strip('\n') for line in lines]



