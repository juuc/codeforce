# C. Save More Mice
for step in range(int(input())):
    n, k = map(int,input().split())
    mices = list(map(int,input().split()))
    left = []
    for mice in mices:left.append(n - mice)
    ans = 0
    limit = 0
    left.sort()
    for i in range(k):
        limit += left[i]
        if limit > n-1:
            break
        ans += 1
    print(ans)