#!/usr/bin/python

inputfile = open('input','r')

total = 0
itts = 0
freq = {}

while 1:
    print "rounding, current total", total, " itts: ", itts
    itts += 1
    for row in inputfile:
        total += int(row)
        if total in freq:
            print "Got it: ", total
            exit()
        else:
            freq[total] = 1
    inputfile.seek(0)
