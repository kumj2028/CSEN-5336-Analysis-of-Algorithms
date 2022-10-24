def insertionSort(A):
    for i in range(1, len(A)):
        j = i
        while j > 0 and A[j - 1] > A[j]:
            A[j], A[j - 1] = A[j - 1], A[j]
            j -= 1
    return A

def bucketSort(A, A_min, A_max):
    A_range = A_max - A_min
    A_len = len(A)
    B = [[] for i in range(A_len)]
    for a in A:
        i = int(A_len * (a - A_min) / A_range)
        # Since bucket sort assumes interval is [0, 1)
        # but randint(1, N) doesn't exclude N
        if i == A_len:
            i -= 1
        B[i].append(a)
    for b in B:
        insertionSort(b)
    C = [c for b in B for c in b]
    return C

def median(A, A_min, A_max):
    C = bucketSort(A, A_min, A_max)
    if len(A) % 2 == 1:
        return C[len(A) // 2]
    else:
        return (C[len(A) // 2] + C[len(A) // 2 - 1]) / 2

import random

N = 5000000
randmatrix = [0]*1000000
for i in range(1000000):
     randmatrix[i] = random.randint(1, N)

m = median(randmatrix, 1, N)
print(m)

import statistics

m2 = statistics . median ( randmatrix )
print(m2)