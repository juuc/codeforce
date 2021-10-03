# B. Hemose Shopping
for step in range(int(input())):
    n, x = map(int,input().split())
    nums = list(map(int,input().split()))
    is_yes= False
    if n//2 >= x:
        is_yes = True
    else:
        if nums[n-x:x] == sorted(nums)[n-x:x]:
            is_yes = True
    print('YES' if is_yes else 'NO')