import sys
import os
import itertools
from StringIO import StringIO

from coding import encode, decode
from interface import dump, load, dumps, loads

def check(s):
    c = encode(s)
    s2 = decode(c)
    assert '\n' not in c[:-1]
    assert c[-1] == '\n'
    assert s == s2

def test_plain():
    check('abcdefg')

def test_zeros():
    check('0')
    check('00')
    check('000')
    check('0000')
    check('00000')

def test_newlines():
    check('\n')
    check('\n\n')
    check('\n\n\n')
    check('\n\n\n\n')
    check('\n\n\n\n\n')

def test_mixed():
    L = 5
    for chars in itertools.product(*[('a', '0', '\n')]*L):
        check("".join(chars))

def test_random_bytes():
    check(os.urandom(10**6))

def test_string_dump_load():
    obj_A = ([1, 3.4, "a"],
             {"a" : 0, 0.1 : []},
             ("abcde\nfeghij\n", ()))
    obj_B = {500 : [1, 3, 4, ("x", "y", "z")]}
    for protocol in [0, 1, 2]:
        s = StringIO()
        s.write(dumps(obj_A))
        s.write(dumps(obj_B))
        s.seek(0)
        newobj_A = loads(s.readline())
        newobj_B = loads(s.readline())
        assert newobj_A == obj_A
        assert newobj_B == obj_B

def test_file_dump_load():
    obj_A = ([1, 3.4, "a"],
             {"a" : 0, 0.1 : []},
             ("abcde\nfeghij\n", ()))
    obj_B = {500 : [1, 3, 4, ("x", "y", "z")]}
    for protocol in [0, 1, 2]:
        s = StringIO()
        dump(obj_A, s)
        dump(obj_B, s)
        s.seek(0)
        newobj_A = load(s)
        newobj_B = load(s)
        assert newobj_A == obj_A
        assert newobj_B == obj_B
