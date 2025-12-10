import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.agrv:
    print("Hello, my name is", arg)