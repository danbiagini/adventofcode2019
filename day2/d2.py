#!/usr/bin/python

inputfile = open('input','r')
#inputfile = open('input-test','r')

total2 = 0
total3 = 0

row_letters = {}


for row in inputfile:
    print row
    for c in row:
        if c in row_letters:
            row_letters[c] += 1
            print "another ", c, " , that's:", row_letters[c]
        else:
            print "first ", c
            row_letters[c] = 1

    row2 = True
    row3 = True
    for k in row_letters.keys():
        if row_letters[k] == 2 and row2:
            total2 += 1
            print "two ", k, " which makes:", total2
            row2 = False
        elif row_letters[k] == 3 and row3:
            total3 += 1
            print "three ", k, " which makes:", total3
            row3 = False

    row_letters.clear()

print "2s:", total2, " 3s:", total3, " checksum: ", total2 * total3
