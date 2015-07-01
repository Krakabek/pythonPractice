__author__ = 'Danil Radkovsky'

import sys
import math
try:
    infilename = sys.argv[1]
    outfilename = sys.argv[2]
except:
    print "Usage:", sys.argv[0], "infile outfile"
    sys.exit(1)

ifile = open(infilename, "r")
ofile = open(outfilename, "w")
def average(pair):
    sum = 0.0
    for num in pair:
        sum += float(num)
    return sum/len(pair)

for line in ifile:
    pair = line.split()
    avg = average(pair)
    for num in pair:
        ofile.write("%12.6f" % float(num))
    ofile.write("%12.6f\n" % avg)

ifile.close()
ofile.close()
