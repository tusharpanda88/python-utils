def printme(argone, *tuple1 ):
	if (not tuple1):
		print "1 argument passed"
		print argone
	else:
		counter = 0
		for var in tuple1:
			counter = counter+1
		print counter+1,"arguments passed"
		print argone,tuple1
		return;

printme(10);
printme(10,'cat',50);

