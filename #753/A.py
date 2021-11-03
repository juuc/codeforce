for step in range(int(input())):
  keyboard = input()
  target = input()
  ans = 0
  for i in range(len(target)-1):
    ans += abs(keyboard.find(target[i])-keyboard.find(target[i+1]))
  print(ans)