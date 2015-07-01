__author__ = 'Danil Radkovsky'
import random as r
import sys


if __name__ == '__main__':
    for i in range(0, int(sys.argv[1])):
        print(-1 + 2 * r.random())
