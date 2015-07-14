import re

"""
We want each invocation of line_pickle.dump to produce a string containing
exactly one linefeed, at the end of the string. So we encode all existing
linefeeds as 0n and existing 0 chars as r'00'.
"""

def encode_match(match):
    c = match.group()
    if c == '0':
        return '00'
    elif c == '\n':
        return '0n'
    else:
        raise Exception("Unexpected character {0}".format(repr(c)))

def decode_match(match):
    c = match.group()
    if c == '00':
        return '0'
    elif c == '0n':
        return '\n'
    else:
        raise Exception("Unexpected character {0}".format(repr(c)))

def encode(string):
    return re.compile('(\n|0)').sub(encode_match, string) + "\n"

def decode(string):
    return re.compile('(00|0n)').sub(decode_match, string[:-1])
