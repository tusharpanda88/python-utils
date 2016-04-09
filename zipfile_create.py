import sys
import zipfile

if __name__ == '__main__':
	zf = zipfile.PyZipFile('t1.zip', mode='w')
	try:
		zf.writepy('.')
		zf.write('input.txt')
		zf.write('test.txt')
	finally:
		zf.close()
	for name in zf.namelist():
		print name


