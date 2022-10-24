def lcs_bottom_up(s1, s2):
    c = [[0]*len(s2) for i in range(len(s1))]
    s = [['']*len(s2) for i in range(len(s1))]

    for i in range(1, len(s1)):
        for j in range(1, len(s2)):
            if s1[i] == s2[j]:
                c[i][j] = c[i-1][j-1] + 1
                s[i][j] = s[i-1][j-1] + s1[i]
            else:
                if c[i][j-1] > c[i-1][j]:
                    c[i][j] = c[i][j-1]
                    s[i][j] = s[i][j-1]
                else:
                    c[i][j] = c[i-1][j]
                    s[i][j] = s[i-1][j]
    return s[-1][-1]

def lcs_top_down(s1, s2):
    memo = [[-1]*len(s2) for i in range(len(s1))]
    result = [['']*len(s2) for i in range(len(s1))]
    def lcs(i, j):
        if i == 0:
            return 0
        if j == 0:
            return 0
        if memo[i][j] != -1:
            return memo[i][j]
        if s1[i] == s2[j]:
            memo[i][j] = 1 + lcs(i-1, j-1)
            result[i][j] = result[i-1][j-1] + s1[i]
            return memo[i][j]
        else:
            a = lcs(i, j-1)
            b = lcs(i-1, j)
            if a > b:
                memo[i][j] = a
                result[i][j] = result[i][j-1]
            else:
                memo[i][j] = b
                result[i][j] = result[i-1][j]
            return memo[i][j]
    lcs(len(s1)-1, len(s2)-1)
    return result[-1][-1]
    

if __name__ == '__main__':
    s1 = ''
    s2 = ''
    with open('DNA1.txt', 'r') as f:
        s1 = f.read().rstrip()
    with open('DNA2.txt', 'r') as f:
        s2 = f.read().rstrip()
    import time
    bottom_up_start = time.perf_counter()
    bottom_up_result = lcs_bottom_up(s1, s2)
    bottom_up_end = time.perf_counter()
    print("Bottom up took %f seconds and result is %s"
    % (bottom_up_end-bottom_up_start, bottom_up_result))
    top_down_start = time.perf_counter()
    top_down_result = lcs_top_down(s1, s2)
    top_down_end = time.perf_counter()
    print("Top down took %f seconds and result is %s"
    % (top_down_end-top_down_start, top_down_result))