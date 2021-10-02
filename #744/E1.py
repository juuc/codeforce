# p m in deque
from collections import deque
for case in range(int(input())):
    n = int(input())
    nums = deque(list(map(int,input().split())))
    ans = deque()
    for _ in range(n):
        cur = nums.popleft()
        if ans:
            if ans[0] > cur:
                ans.appendleft(cur)
            else:ans.append(cur)
        else:ans.append(cur)
    print(*ans)