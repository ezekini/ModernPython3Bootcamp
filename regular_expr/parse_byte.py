'''
parse_bytes("11010101 101 323")    # ['11010101']
parse_bytes("my data is: 10101010 11100010")   # ['10101010', '11100010']
parse_bytes("asdsa")   # []

'''
import re

# Returns first instance of phone number pattern:


def parse_bytes(input):
    byte_pat = re.compile(r'\b[01]{8}\b')
    match = byte_pat.findall(input)
    return match


# parse_bytes('11010101 101 323')
# parse_bytes('my data is: 10101010 11100010')
# parse_bytes('asdsa')
