# D productive meetings
import heapq
for case in range(int(input())):
    ans = 0
    n = int(input())
    soci = list(map(int,input().split()))
    soci_maxheap = [(-i,i,idx+1) for idx,i in enumerate(soci)]
    heapq.heapify(soci_maxheap)
    out = []
    while True:
        maxi = heapq.heappop(soci_maxheap) # 최댓값
        maxi_2 = heapq.heappop(soci_maxheap) # 2번째 최댓값
        if maxi_2[0] == 0:
            break
        out.append((maxi[2],maxi_2[2]))
        after = (maxi[0]+1,maxi[1],maxi[2])
        after_2 = (maxi_2[0]+1,maxi_2[1],maxi_2[2])
        ans += 1
        heapq.heappush(soci_maxheap,after)
        heapq.heappush(soci_maxheap,after_2)
    print(ans)
    for i in out:print(*i)