for step in range(int(input())):
  r, c = map(int,input().split())
  commands = input()
  lm, rm, um, dm = 0, 0, 0, 0
  xpos, ypos = 0, 0
  broken = False
  for i in range(len(commands)):
    if commands[i] == 'R':
      xpos += 1
      rm = max(xpos,rm)
    if commands[i] == 'L':
      xpos -= 1
      if xpos<=0:
        lm = min(xpos,lm)
    if commands[i] == 'U':
      ypos += 1
      um = max(ypos,um)
    if commands[i] == 'D':
      ypos -= 1
      if ypos<=0:
        dm = min(ypos,dm)
  
    if rm - lm == c or um - dm == r:
      broken = True
      break
  if broken:
    if commands[i] == 'U':
      um -= 1
    if commands[i] == 'R':
      rm -= 1
  print(um+1,c-rm)