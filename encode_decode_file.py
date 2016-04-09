#base64 encoding/decoding file
import base64
file1 = open("file1","w")
file1.write("how r u")
file1.close()
base64.encode(open("file1"),open("file1.64","w"))
base64.decode(open("file1.64"),open("file2","w"))
