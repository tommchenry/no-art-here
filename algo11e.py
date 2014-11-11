#!/usr/bin/env python

"""
This is Algorithm 1.1E (Euclid's Algorithm) from Knuth's Art of Computer
Programming.
"""
def euclid(m,n):
    print "M: ", m
    print "N: ", n
    if m%n == 0:
        print "The greatest common divisor: ",n
    else: 
        r = m%n
        print "R: ", r 
        euclid (n,r)

euclid(556,378)


# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
