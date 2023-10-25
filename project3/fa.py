import time

alpha = {'A': 0, 'T' : 1, 'G' : 2, 'C' : 3}
pmod = 13

def fa(text, pattern):
    plen = len(pattern)
    tf = compute