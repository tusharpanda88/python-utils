##unicode/encode/decode

import binascii

convert text nbyte string.
def to_hex(t, nbytes):
    chars_per_item = nbytes * 2
    hex_version = binascii.hexlify(t)
    return ' '.join(
        hex_version[start:start + chars_per_item]
        for start in xrange(0, len(hex_version), chars_per_item)
        )

if __name__ == '__main__':
    print to_hex('abcdef', 1)
    print to_hex('abcdef', 3)
