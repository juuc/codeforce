# B. Diameter of Graph
for step in range(int(input())):
    n,m,k = map(int,input().split())
    if m > n*(n-1)//2 or m < n-1: 
        print('NO')
    elif k == 0 or k == 1: print('NO')
    elif k == 2: print('YES' if (n,m) == (1,0) else 'NO')
    # diameter should be less than k-1
    elif m == n*(n-1)//2 and k > 2: print('YES') # diameter = 1
    else: print('YES' if 2 < k-1 else 'NO') # diameter = 2