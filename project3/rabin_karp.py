SigMap = {'A': 0, 'T' : 1, 'G' : 2, 'C' : 3}
PriMod = 13

def rabin_karp(text, pattern):
    matches = []
    plen = len(pattern)
    phash = rabin_hash(pattern)
    for i in range(0, len(text) - len(pattern)):
        if i == 0:
            thash = rabin_hash(text[0:len(pattern)])
        else:
            thash = roll(plen, thash, 
                            text[i - 1], text[i + plen - 1])
        if thash == phash:
            if text[i:i+plen] == pattern:
                matches.append(i)
    return matches

def rabin_hash(text):
    rhash = 0
    for c in text:
        rhash = (rhash * len(SigMap) % PriMod + SigMap[c]) % PriMod
    return rhash

def roll(plen, oldhash, oldchar, newchar):
    newhash = ((oldhash + PriMod 
                - SigMap[oldchar] * (len(SigMap) ** (plen - 1)) % PriMod) 
                * len(SigMap) + SigMap[newchar]) % PriMod
    return newhash

import time
if __name__ == '__main__':
    text = ''
    patterns = ['ACT', 'GATTACA', 'CATCATCATCAT']
    for fname in ['DNA1.txt', 'DNA2.txt', 'DNA3.txt','DNA4.txt', 'DNA5.txt']:
        with open(fname, 'r') as f:
            text = f.read().rstrip()
        for pattern in patterns:
            start_time = time.perf_counter()
            matches = rabin_karp(text, pattern)
            end_time = time.perf_counter()
            print(f'For {fname} and pattern {pattern}, the Rabin-Karp algorithm took {end_time-start_time} seconds with {len(matches)} matches')
