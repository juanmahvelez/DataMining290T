#!/usr/bin/python
"""This script can be used to analyze data in the 2012 Presidential Campaign,
available from ftp://ftp.fec.gov/FEC/2012/pas212.zip - data dictionary is at
http://www.fec.gov/finance/disclosure/metadata/DataDictionaryContributionstoCandidates.shtml
"""

import fileinput
import csv

total = 0.0

for row in data:
    #if not fileinput.isfirstline():
    amt = float(row[14])
    total += amt
    amtarray.append(amt)
    cand = row[16]
    candarray.append(cand)
    
amtsorted = sorted(amtarray)
minimum = amtsorted[0]
maximum = amtsorted[len(amtsorted)-1]
mean = total/len(amtsorted)
median = amtsorted[(len(amtsorted)-1)/2]

sqerrorarray = [(x - mean)**2 for x in amtarray]
for sqerror in sqerrorarray:
    sumerror += sqerror
sigma = (sumerror/(len(amtsorted)-1))**0.5

candidates = len(set(candarray))


##### Print out the stats
print "Total: %s" % total
print "Minimum: " , minimum
print "Maximum: " , maximum
print "Mean: " , mean
print "Median: " , median
# square root can be calculated with N**0.5
print "Standard Deviation: " , sigma

##### Comma separated list of unique candidate ID numbers
print "Candidates: " , candidates

def minmax_normalize(value):
    """Takes a donation amount and returns a normalized value between 0-1. The
    normilzation should use the min and max amounts from the full dataset"""
    
    norm = ((value - minimum)/(maximum - minimum))
    return norm

    return norm

##### Normalize some sample values
print "Min-max normalized values: %r" % map(minmax_normalize, [2500, 50, 250, 35, 8, 100, 19])
