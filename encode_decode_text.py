

#base64 encoding/decoding text
import base64
string_orig = "tushar"
string_enc = base64.encodestring(string_orig)
string_dec = base64.decodestring(string_enc)
print string_orig
print string_enc
print string_dec

