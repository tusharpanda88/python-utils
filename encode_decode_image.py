
#base64 encoding/decoding image/picture/photo
import base64
imageFile = open("failure.png", "rb")
str = base64.b64encode(imageFile.read())
fh = open("file1", "w")
fh.write(str)
fh.close()

fh = open("file1", "r")
str3 = fh.read()
fh.close()
fh = open("image2.jpg", "wb")
fh.write(str3.decode('base64'))
fh.close()
