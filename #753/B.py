for step in range(int(input())):
  x, n = map(int,input().split())
  if not x&1: 
    if n%4 == 0: print(x)
    elif n%4 == 1: print(x-n)
    elif n%4 == 2: print(x+1)
    elif n%4 == 3: print(x+n+1)
  else:
    if n%4 == 0: print(x)
    elif n%4 == 1: print(x+n)
    elif n%4 == 2: print(x-1)
    elif n%4 == 3: print(x-n-1)