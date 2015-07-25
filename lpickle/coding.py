import re

"""
We want each invocation of line_pickle.dump to produce a string containing
exactly one linefeed, at the end of the string. So we encode all existing
linefeeds as '0n' and existing '0' chars as '00'.
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

encode_re= re.compile('(\n|0)')
def encode(string):
    return encode_re.sub(encode_match, string) + "\n"

decode_re = re.compile('(00|0n)')
def decode(string):
    return decode_re.sub(decode_match, string[:-1])
