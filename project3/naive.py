def naive(text, pattern):
    matches = []
    for i in range(0, len(text) - len(pattern)):
        found = True
        for j in range(len(pattern)):
            if text[i+j] != pattern[j]:
                found = False
                break
        if found == True:
            matches.append(i)
    return matches

import time
if __name__ == '__main__':
    text = ''
    patterns = ['ACT', 'GATTACA', 'CATCATCATCAT']
    for fname in ['DNA1.txt', 'DNA2.txt', 'DNA3.txt','DNA4.txt', 'DNA5.txt']:
        with open(fname, 'r') as f:
            text = f.read().rstrip()
        for pattern in patterns:
            start_time = time.perf_counter()
            matches = naive(text, pattern)
            end_time = time.perf_counter()
            print(f'For {fname} and pattern {pattern}, the naive algorithm took {end_time-start_time} seconds with {len(matches)} matches')
