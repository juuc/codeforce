# E2. Array Optimization by Deque
# 펜윅트리
# https://yabmoons.tistory.com/438
##################
import sys
for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    d = [int(i) for i in sys.stdin.readline().split()][:n]
    s = sorted(d)

    # input을 1부터 1 간격으로 압축해서 나타내기
    dd, last = {}, 1
    for i in s:
        if not i in dd:
            dd[i] = last
            last+=1
    d = [dd[i] for i in d] 
    a = [0]*(n+1)

    def qry(x): 
        r = 0
        while x > 0:
            r+=a[x]
            x -= x&(-x)
        return r

    def update(x):
        while x <= n:
            a[x]+=1 # 1이 아니고 value라면? 일반적인 펜윅트리
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

# query는 나보다 작은 수가 몇 개 있었는지에 대해 체크할 수 있음
# 1이 들어가면 -> query 1 체크, 1, 10, 100, 1000에 update
# 4가 들어가면 -> query 100 체크,  100, 1000에 update
# 3이 들어가면 -> query 11, 10 체크, 11, 100, 1000에 update
# 5가 들어가면 -> query 101, 100 체크, 101, 110, 1000에 update
# 2가 들어가면 -> query 10 체크, 10, 100, 1000에 update