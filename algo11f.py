#!/usr/bin/env python

"""
Euclid's algorithm refined (Algorithm F)
Removes the additional variable r.
"""
def euclid2(m,n):
    m = m%n
    if m == 0: 
        print "Greatest Common Divisor:", n
    else: 
        euclid2(n,m)

euclid2(6099,2166)

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
