import pickle
from coding import encode, decode
from cStringIO import StringIO

def dump(obj, file, protocol=1):
    file.write(dumps(obj, protocol))

def dumps(obj, protocol=1):
    return encode(pickle.dumps(obj, protocol))

def load(file):
    return load_line(file.readline())

def loads(string):
    return load_line(StringIO(string).readline())

def load_line(line):
    return pickle.loads(decode(line))
