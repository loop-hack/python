#using sys

import sys

print("hello, my name is",sys.argv[1])

#to overcome IndexError if user say python name.py 

import sys

if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else :
    print("hello, my name is", sys.argv[1])

#using sys.exit if error heppens like too many/few arguments

import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print("hello, my name is", sys.argv[1])



#creating code without any restriction of maximum number of arguments

import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv:
    print("hello, my name is",arg)


#fixing bugs using slice as in previos case name.py was included

import sys

if len(sys.argv)<2:
    print("Too few arguments")

for arg in sys.argv[1:]:
    print("Hello, my name is", arg)