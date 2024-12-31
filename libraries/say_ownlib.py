# importing hello() function from sayings.py{my own created lib}

import sys
from sayings import hello

if len(sys.argv) == 2:
    hello(sys.argv[1])

#using goodbye() funstion

import sys
from sayings import goodbye
if len(sys.argv) == 2:
    goodbye(sys.argv[1])