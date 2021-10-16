import sys
def prime_list(n):
    sieve = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:          
            for j in range(i+i, n, i):
                sieve[j] = False
    return [i for i in range(2, n) if sieve[i] == True]

input = sys.stdin.readline
for step in range(int(input())):
    n, c = input().split()
    n = int(n)
    s = input().strip()
    visited = 0
    for idx,i in enumerate(s):
        if i == c:
            visited += (1 << idx)
    ans = []
    # until visited = 1111...111
    esc = (1<<n) -1
    pri = [1] + prime_list(n+1)
    i = 0
    while esc!=visited&esc:
        # pri[i] is x
        cnt = False
        # finding i (j is i)
        for j in range(n):
            if not visited & (1<<j) and (j+1)%pri[i]:
                visited += (1<<j)
                cnt = True
        if cnt: ans.append(pri[i])
        i += 1
    print(len(ans))
    if ans:print(*ans)