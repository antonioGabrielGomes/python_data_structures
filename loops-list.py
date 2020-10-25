nlist = list()

while True:
 inp = input('Enter a number: ')
 if inp == 'done' : 
  print(inp)
  break
 value = float(inp)
 nlist.append(value)

average = sum(nlist) / len(nlist)
print('Average:', average)
