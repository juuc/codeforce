# C. ticks
def check(board,ticks,k):
    painted = set()
    for row,col in ticks:
        tmp = set()
        leg = 0 # tick의 길이 (0일때 한칸, 1일때 2칸 v 모양)
        while True:
            if 0<=row-leg and 0<=col-leg and col+leg<=m-1 and board[row-leg][col-leg] == '*' and board[row-leg][col+leg] == '*':
                tmp.add((row-leg,col-leg))
                tmp.add((row-leg,col+leg))
                leg += 1
            else:
                if leg-1 >= k: # leg - 1이 k 이상인 것만 색칠하고 아닌건 넘어가기(tmp에 기록했을 때의 leg보다 1 커져서 else에 들어옴)
                    painted = painted.union(tmp)
                break
    for coord in ticks: # tick의 좌표 coord = (x,y)가 painted에 있으면 그릴 수 있음
        if coord not in painted:
            return False
    return True

for case in range(int(input())):
    n, m, k = map(int,input().split())
    board = [[] for _ in range(n)]
    ticks_removed = set()
    ticks = []
    for i in range(n):
        tmp = input()
        for idx, letter in enumerate(tmp):
            if letter == '*':
                ticks.append((i,idx)) # memory of (row,col) of tick
            board[i].append(letter)
    print('YES' if check(board,ticks,k) else 'NO')