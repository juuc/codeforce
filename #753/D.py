for step in range(int(input())):
  n = int(input())
  marbles = list(map(int,input().split()))
  colors = input()
  redMarbles = []
  blueMarbles = []
  for i in range(n):
    if colors[i] == 'B': blueMarbles.append(marbles[i])
    else: redMarbles.append(marbles[i])
  
  redMarbles.sort(reverse=True)
  blueMarbles.sort()

  ans = True
  for i in range(len(redMarbles)):
    if redMarbles[i] > n-i: ans = False
  for i in range(len(blueMarbles)):
    if blueMarbles[i] <= i: ans = False
  print('YES' if ans else 'NO')