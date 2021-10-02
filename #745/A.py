# A. CQXYM Count Permutations
def calc(n,mod=10**9+7):
    return (((dp[-1] * ((n-1)%mod))%mod)*(n%mod))%mod
dp = [1]
for i in range(2,10**5+1):
    dp.append(calc(2*i))
for _ in range(int(input())):
    print(dp[int(input())-1])