def kmp(text, pattern):
    matches = []
    m = len(pattern)
    n = len(text)
    pfxfun = getPrefixFunction(pattern)
    i = 0
    j = 0

    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == m:
                matches.append(i-j)
                j = pfxfun[j-1]
        else:
            if j > 0:
                j = pfxfun[j-1]
            else:
                i += 1

    return matches

def getPrefixFunction(pattern):
    pfxfun = [0 for i in range(len(pattern))]
    i = 1
    j = 0
    while i < len(pattern):
        if pattern[i] == pattern[j]:
            j += 1
            pfxfun[i] = j
            i += 1
        else:
            if j != 0:
                j = pfxfun[j - 1]
            else:
                pfxfun[i] = 0
                i += 1
    return pfxfun

import time
if __name__ == '__main__':
    text = ''
    patterns = ['ACT', 'GATTACA', 'CATCATCATCAT']
    for fname in ['DNA1.txt', 'DNA2.txt', 'DNA3.txt','DNA4.txt', 'DNA5.txt']:
        with open(fname, 'r') as f:
            text = f.read().rstrip()
        for pattern in patterns:
            start_time = time.perf_counter()
            matches = kmp(text, pattern)
            end_time = time.perf_counter()
            print(f'For {fname} and pattern {pattern}, the Knuth-Morris-Pratt algorithm took {end_time-start_time} seconds with {len(matches)} matches')
