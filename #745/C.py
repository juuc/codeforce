# C. Portal
for _ in range(int(input())):
    row, col = map(int,input().split())
    board = []
    for i in range(row):
        board.append(input())
def find(trow,tcol):
    global row,col
    ans = 1e6
    for i in range(row-trow+1):
        for j in range(col-tcol+1):
            tmp_ans = 0
            for dy in range(trow):
                for dx in range(tcol):
                    if (dx,dy) in [(0,0),(trow-1,0),(0,tcol-1),(trow-1,tcol-1)]:
                        pass
                    elif dy == 0 or dy == trow-1 or dx == 0 or dx == tcol-1:
                        if board[i+dy][j+dx] == '0':
                            tmp_ans += 1
                    else:
                        if board[i+dy][j+dx] == '1':
                            tmp_ans += 1
            ans = min(tmp_ans,ans)
    return ans
ans = 1e6
for rowsize in range(5,row+1):
    for colsize in range(4,col+1):
        print(rowsize,colsize)
        ans = min(ans,find(rowsize,colsize))
print(ans)