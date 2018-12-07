#!/usr/bin/python

import sys
import os

file = sys.argv[1]

inputfile = open(file,'r')

lines = []

for row in inputfile:
    lines.append(row)


print len(lines)

for i in range(0, len(lines)):
    for j in range(i, len(lines)):
        s1 = lines[i]
        s2 = lines[j]
        no_match = 0
        for ci in range(0, len(s1)):
            if s1[ci] != s2[ci]:
                no_match += 1
            if no_match > 1:
                print "s1:", s1, " > 2 mismatches:", s2
                break
        if no_match == 1:
            print "Got it: ", s1, " and ", s2
            exit()
