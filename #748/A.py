# A. Elections
for step in range(int(input())):
    a, b, c = map(int,input().split())
    maxi = max([a,b,c])
    if a==b and b==c: print(1,1,1)
    else:
        if a==b and b<c: print(maxi-a+1,maxi-b+1,0)
        elif a==b and b>c: print(1,1,maxi-c+1)
        elif b==c and a>b: print(0,maxi-b+1,maxi-c+1)
        elif b==c and a<b: print(maxi-a+1,1,1)
        elif a==c and a>b: print(1,maxi-b+1,1)
        elif a==c and a<b: print(maxi-a+1,0,maxi-c+1)
        else:
            resi_a = maxi - a
            resi_b = maxi - b
            resi_c = maxi - c
            if resi_a == 0: print(0,resi_b+1,resi_c+1)
            elif resi_b == 0: print(resi_a+1,0,resi_c+1)
            elif resi_c == 0: print(resi_a+1,resi_b+1,0)