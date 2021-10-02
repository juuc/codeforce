n = int(input())
for step in range(n):
    word = input()
    numofA = word.count('A')
    numofB = word.count('B')
    numofC = word.count('C')
    if numofC + numofA == numofB:print('Yes')
    else:print('No')