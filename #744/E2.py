# E2. Array Optimization by Deque
# 펜윅트리
# https://yabmoons.tistory.com/438
##################
import sys
for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    d = [int(i) for i in sys.stdin.readline().split()][:n]
    s = sorted(d)
    dd, last = {}, 1
    for i in s:
        if not i in dd:
            dd[i] = last
            last+=1
    d = [dd[i] for i in d]
    a = [0]*(n+1)

    def qry(x): 
        r = 0
        while x > 0: # x로 인해 영향을 받는 노드가 바로 a[x]들
            r+=a[x]
            x -= x&(-x)
        return r

    def update(x):
        while x <= n:
            a[x]+=1
            x += x&(-x)

    r = 0
    dd = [0]*(n+1)
    for i in range(n):
        q = qry(d[i])
        print(a)
        print(d[i], q-dd[d[i]], i-q)
        r += min(q-dd[d[i]], i - q)
        dd[d[i]]+=1
        update(d[i])
    print('%d'%r)