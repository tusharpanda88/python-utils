#http://stackoverflow.com/questions/1207457/convert-a-unicode-string-to-a-string-in-python-containing-extra-symbols

##
import binascii
text1 = "tushar"
text2 = binascii.hexlify(text1)
text3 = binascii.unhexlify(text2)
print "original",text1
print "string to hex",text2
print "hex to string",text3

#web input unicode to ascii
raw_data.encode('ascii','ignore')
unicodedata.normalize('NFKD', raw_data).encode('ascii','ignore')


##
unicodestring = u"Hello world"

# Convert Unicode to plain Python string: "encode"
utf8string = unicodestring.encode("utf-8")
asciistring = unicodestring.encode("ascii")
isostring = unicodestring.encode("ISO-8859-1")
utf16string = unicodestring.encode("utf-16")

# Convert plain Python string to Unicode: "decode"
plainstring1 = unicode(utf8string, "utf-8")
plainstring2 = unicode(asciistring, "ascii")
plainstring3 = unicode(isostring, "ISO-8859-1")
plainstring4 = unicode(utf16string, "utf-16")
assert plainstring1 == plainstring2 == plainstring3 == plainstring4

