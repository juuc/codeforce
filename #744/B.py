for step in range(int(input())):
    length = int(input())
    nums = list(map(int,input().split()))
    idx = 1
    actions = []
    correct = sorted(nums)
    cnt = 0
    while nums != correct:
        for idx in range(length):
            if nums[idx] == correct[idx]:
                continue
            else:
                l = idx
                r = nums.index(correct[idx],l)
                break
        d = r-l
        tmp = nums[l:r+1]
        new = []
        for ind in range(r-l+1):
            new.append(tmp[(d+ind)%(r-l+1)])
        nums = nums[:l] + new + nums[r+1:]
        actions.append((l+1,r+1,d))
        cnt += 1
    print(cnt)
    for action in actions:
        print(*action)