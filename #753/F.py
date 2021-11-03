def start(cr,cc,r,c):
  visited = [[False] * c for _ in range(r)]
  visited[cr][cc] = True
  d = 0
  q = []
  q.append((cr,cc))
  while q:
    cr,cc = q.pop()
    if board[cr][cc] == 'R':
      nc = cc+1
      nr = cr
    if board[cr][cc] == 'L':
      nc = cc-1
      nr = cr
    if board[cr][cc] == 'U':
      nr = cr-1
      nc = cc
    if board[cr][cc] == 'D':
      nr = cr+1
      nc = cc
    if 0<=nr<=r-1 and 0<=nc<=c-1 and not visited[nr][nc]:
      d += 1
      q.append((nr,nc))
      notanswer[cr*c+cc] = True
      visited[nr][nc] = True
  # 최대 방문 횟수 리턴
  return d

for step in range(int(input())):
  input()
  r, c = map(int,input().split())
  board = [list(input()) for _ in range(r)]
  ans = 0
  anspos = (0,0)
  # 한번 방문했던 곳이면 정답 위치가 아닐 것이므로 pass하기 위해서
  notanswer = [False]*(c*r)

  for i in range(r):
    for j in range(c):
      if not notanswer[i*c+j]:
        ret = start(i,j,r,c)
        if ans < ret:
          ans = ret
          anspos = (i,j)
  
  # 정답 좌표와 정답 길이 출력
  print(anspos[0]+1,anspos[1]+1,ans+1)