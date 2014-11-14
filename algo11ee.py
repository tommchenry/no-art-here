#!/usr/bin/env python

"""
Algorithm E (Extended Euclid's algorithm)
"""
def extendEuclid(m,n):
    aprime = 1
    b = 1
    a = 0
    bprime = 0
    c = m
    d = n
    running = True
    while running == True:
        q = c/d 
        r = c%d
        if r == 0: 
            print "a': %d a: %d b': %d b: %d c: %d d: %d q: %d r: %d" % (aprime,a,bprime,b,c,d,q,r)
            print "Algorithm Terminates"
            print "%d(%d) + %d(%d) = %d" % (a,m,b,n,d)
            running = False
        else: 
            print "a': %d a: %d b': %d b: %d c: %d d: %d q: %d r: %d" % (aprime,a,bprime,b,c,d,q,r)
            c = d
            d = r
            t = aprime
            aprime = a
            a = t - q*a
            t = bprime
            bprime = b
            b = t - q*b

extendEuclid(1769,551)

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
