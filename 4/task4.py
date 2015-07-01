__author__ = 'Danil Radkovsky'

import sys
import math

def print_ln(arg):
    num = float(arg)
    if num > 0:
        print("ln(%g) = %g" % (num, math.log(num)))
    else:
        print("ln(%g) is illegal" % num)
if __name__ == '__main__':
    for r in sys.argv[1:]:
        print_ln(r)

    for i in range(1, len(sys.argv)):
        print_ln(sys.argv[i])

    i = 1
    while i < len(sys.argv):
        print_ln(sys.argv[i])
        i += 1
    i = 1
    while 1:
        try:
            print_ln(sys.argv[i])
            i += 1
        except LookupError:
            break

