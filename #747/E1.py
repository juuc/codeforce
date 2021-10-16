n = int(input())
ans = (1<<n) - 2
mod = 10**9+7
answer = 1
mod_dp = [4**2]
for i in range(2,n):
    mod4power = (mod_dp[-1] * mod_dp[-1] * mod_dp[0])%mod
    mod_dp.append(mod4power)
if n==1:print(6)
elif n==2:print(96)
else:print((6*mod_dp[-1])%mod)