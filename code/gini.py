#!/usr/bin/python
"""Script can be used to calculate the Gini Index of a column in a CSV file.

Classes are strings."""

import fileinput
import csv
import collections
import itertools

(
    CMTE_ID, AMNDT_IND, RPT_TP, TRANSACTION_PGI, IMAGE_NUM, TRANSACTION_TP,
    ENTITY_TP, NAME, CITY, STATE, ZIP_CODE, EMPLOYER, OCCUPATION,
    TRANSACTION_DT, TRANSACTION_AMT, OTHER_ID, CAND_ID, TRAN_ID, FILE_NUM,
    MEMO_CD, MEMO_TEXT, SUB_ID
) = range(22)

CANDIDATES = {
    'P80003338': 'Obama',
    'P80003353': 'Romney',
}

############### Set up variables
# TODO: declare datastructures
x = collections.Counter()
y = collections.Counter()
z = collections.Counter()
############### Read through files
data = csv.reader(fileinput.input("../data/itpas2.txt"),delimiter='|')
for row in data:
    candidate_id = row[CAND_ID]
    if candidate_id not in CANDIDATES:
        continue

    candidate_name = CANDIDATES[candidate_id]
    zip_code = row[ZIP_CODE]
    ###
    # TODO: save information to calculate Gini Index
    ##/
    y.update([candidate_name])
    z.update([zip_code])
    if candidate_name == 'Romney':
        x.update([zip_code])


listZipGini = [] 
for i in range(len(z.keys())):

    if x.get(z.keys()[i]) is not None: 
        zipRom = float(x.get(z.keys()[i]))

    else:
        zipRom = 0
    zipObam = float(z.values()[i])-zipRom
    zipTotal = float(z.values()[i])
    zipClasses = [zipRom/zipTotal,zipObam/zipTotal]    
    zipGini = float(1 - sum(frac**2 for frac in zipClasses))
    listZipGini.append(zipGini)


Rom = float(y.values()[0])
Obam = float(y.values()[1])
total = float(sum(y.values()))
classes = [Rom/total,Obam/total]



###
# TODO: calculate the values below:
gini = float(1 - sum(frac**2 for frac in classes))  # current Gini Index using candidate name as the class
split_gini = float(sum(listZipGini)/len(listZipGini))  # weighted average of the Gini Indexes using candidate names, split up by zip code
##/

print "Gini Index: %s" % gini
print "Gini Index after split: %s" % split_gini
