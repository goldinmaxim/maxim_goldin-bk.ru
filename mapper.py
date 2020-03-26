#!/usr/bin/env python
import string
import fileinput

for line in fileinput.input():
    data = line.strip().split("\t")
    if len(data) == 6:
        ip, userid, country, bannerid, payout = data
        print "{0}\t{1}".format(country, payout)
