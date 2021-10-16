# D1. All are Same
def gcd(m,n):
    if m < n :
        m,n = n,m
    while n != 0:
        t = m%n
        (m,n) = (n,t)
    return abs(m)

for step in range(int(input())):
    n = int(input())
    polycarp = list(map(int,input().split()))
    polycarp = list(set(polycarp))
    if len(polycarp) == 1: print(-1)
    else: 
        mini = min(polycarp)
        residuals = []
        for num in polycarp:
            if num - mini != 0:
                residuals.append(num - mini)
        if len(residuals) != 1:
            ans = gcd(residuals[0],residuals[1])
            for idx in range(1,len(residuals)):
                ans = gcd(ans,residuals[idx])
            print(ans)
        else: print(residuals[0])