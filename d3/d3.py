#!/usr/bin/python

import sys
import os
import re

file = sys.argv[1]

inputfile = open(file,'r')

pattern = re.compile("\#(\d+) @ (\d+),(\d+): (\d+)x(\d+)")
grid = dict()
fabric = set()
overlaps = set()
noOverlaps = dict()

def fillGrid():

    for row in inputfile:
        match = re.search(pattern, row)
        if not match:
            print "no match:", row
            exit()

        id = int(match.group(1))
        l_offset = int(match.group(2))
        t_offset = int(match.group(3))
        width = int(match.group(4))
        height = int(match.group(5))
        if (t_offset + height) > 1000:
            print "too tall!! ", row, ":", l_offset, t_offset, width, height
            exit()
        elif (l_offset + width) > 1000:
            print "too wide!! ", row, ":", l_offset, t_offset, width, height
            exit()

        claim = set()
        for y in range(t_offset, t_offset + height):
            xy = y * 1000 + l_offset
            claim.update(range(xy, xy + width))

        grid[id] = claim
#        print claim, fabric
        if fabric.isdisjoint(claim):
            noOverlaps[id] = claim

        overlaps.update(claim & fabric)

#        print "overlaps:", overlaps
        fabric.update(claim)
            
fillGrid()

print "overlaps len:", len(overlaps)

for k,v in noOverlaps.viewitems():
    if overlaps.isdisjoint(v):
        print "no overlap:", k
#    else:
#        del noOverlaps[k]

#print "no overlap:", noOverlaps
