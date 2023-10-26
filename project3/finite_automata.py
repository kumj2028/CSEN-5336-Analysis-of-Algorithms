SigMap = {'A': 0, 'T' : 1, 'G' : 2, 'C' : 3}

def finite_automata(text, pattern):
    matches = []
    m = len(pattern)
    tf = computeTF(pattern)

    state = 0
    for i in range(len(text)):
        state = tf[state][SigMap[text[i]]]
        if state == m:
            matches.append(i-m+1)
    
    return matches

def computeTF(pattern):
    m = len(pattern)
    tf = [[0 for i in range(len(SigMap))] for j in range(m + 1)]
    for state in range(m + 1):
        for c in SigMap:
            nextState = getNextState(pattern, state, c)
            tf[state][SigMap[c]] = nextState
    return tf

def getNextState(pattern, state, c):
    # c matches next character in pattern
    if state < len(pattern) and c == pattern[state]:
        return state + 1
    
    # find longest prefix which is also the suffix
    # of pattern[0:nextState]
    i = 0
    for nextState in range(state, 0, -1):
        if pattern[nextState-1] == c:
            while (i < nextState - 1):
                pfxidx = state - nextState + 1 + i
                if pattern[i] != pattern[pfxidx]:
                    break
                i += 1
            if i == nextState - 1:
                return nextState
    return 0

import time
if __name__ == '__main__':
    text = ''
    patterns = ['ACT', 'GATTACA', 'CATCATCATCAT']
    for fname in ['DNA1.txt', 'DNA2.txt', 'DNA3.txt','DNA4.txt', 'DNA5.txt']:
        with open(fname, 'r') as f:
            text = f.read().rstrip()
        for pattern in patterns:
            start_time = time.perf_counter()
            matches = finite_automata(text, pattern)
            end_time = time.perf_counter()
            print(f'For {fname} and pattern {pattern}, the finite automata algorithm took {end_time-start_time} seconds with {len(matches)} matches')
