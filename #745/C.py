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

from matplotlib import pyplot as plt
freqs = [0,4,2,3,8,24,11,14,5,6]
Xisquare = [(idx*10)**2 * i for idx, i in enumerate(freqs)]; print(sum(Xisquare))
Xi = [(idx*10) * i for idx, i in enumerate(freqs)]; print((sum(Xi)/77))
print(((sum(Xisquare) - sum(Xi)**2/77)/76)**0.5)
xaxis = [0,10,20,30,40,50,60,70,80,90]

from scipy.stats import norm
rv = norm(loc = sum(Xi)/77, scale = ((sum(Xisquare) - sum(Xi)**2/77)/76)**0.5) #평균 0이고 표준편차 1인 정규분포 객체 만들기
(rv.cdf(95) - rv.cdf(85))
plt.plot(xaxis[1:],Xi[1:])