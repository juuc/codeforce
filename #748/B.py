# B. Make it Divisible by 25
import sys
input = sys.stdin.readline
for step in range(int(input())):
    n = input().strip()
    end_5,end_0 = n[:], n[:]
    ans_5 = 0
    ans_0 = 0
    while end_5[-1] != '5' and len(end_5) >= 2:
        end_5 = end_5[:-1]
        ans_5 += 1

    while end_0[-1] != '0' and len(end_0) >= 2:
        end_0 = end_0[:-1]
        ans_0 += 1

    while len(end_5) >= 2 and end_5[-2] not in ('2','7'):
        end_5 = end_5[:-2] + end_5[-1]
        ans_5 += 1
    
    while len(end_0) >= 2 and end_0[-2] not in ('0','5'):
        end_0 = end_0[:-2] + end_0[-1]
        ans_0 += 1

    print(min(ans_5,ans_0))