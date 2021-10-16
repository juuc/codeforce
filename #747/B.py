for step in range(int(input())):
    n, k = map(int,input().split())
    ans = 0
    mod = 10**9+7
    while k>0:
        digit = k & -k
        ans += n**(len(bin(digit))-3)
        ans %= mod
        k -= k & -k
    print(ans)