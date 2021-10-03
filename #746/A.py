for step in range(int(input())):
    n, H = map(int,input().split())
    weapons = list(map(int,input().split()))
    weapons.sort()
    strongest = weapons[-1]
    secstrong = weapons[-2]
    ans = 0
    mog = H // (strongest + secstrong)
    ans += 2*mog
    leftover = H % (strongest + secstrong)
    if 0<leftover <= strongest:ans += 1
    elif leftover == 0: pass
    else:ans += 2
    print(ans)