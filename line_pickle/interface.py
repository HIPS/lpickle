import pickle
from coding import encode, decode
from StringIO import StringIO

def dump(obj, file, protocol=0):
    file.write(dumps(obj, protocol))

def dumps(obj, protocol=0):
    return encode(pickle.dumps(obj, protocol))

def load(file):
    return load_line(file.readline())

def loads(string):
    return load_line(StringIO(string).readline())

def load_line(line):
    return pickle.loads(decode(line))
