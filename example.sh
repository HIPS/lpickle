#!/bin/bash

cat > make_params.py <<EOF
import sys
import lpickle as pickle

for x in range(4):
    sys.stderr.write("Prepping parameter {0}\n".format(x))
    pickle.dump(x, sys.stdout)
EOF

cat > square.py <<EOF
import sys
import os
import lpickle as pickle
x = pickle.load(sys.stdin)
sys.stderr.write("Hello, this is process {0} with data {1}\n".format(os.getpid(), x))
pickle.dump([x, x**2], sys.stdout)
EOF

cat > proclaim_results.py <<EOF
import sys
import lpickle as pickle
for x, x_squared in pickle.stream(sys.stdin):
    print "The square of {0} is {1}".format(x, x_squared)
EOF

python make_params.py | \
parallel --pipe --N 1 python square.py | \
python proclaim_results.py

rm make_params.py square.py proclaim_results.py
