import random
stock = [[i, j] for i in range(7) for j in range(i, 7)]
pl = []
com = []
k = 0
sn = []
status = ('player','computer')


for i in range(14):
  random.shuffle(stock, random.random)
  if stock[i] == [6, 6] or [5, 5]:
    break



for i in range(7):
    pl.append(stock[i])
    stock.remove(stock[i])

for i in range(7):
    com.append(stock[i])
    stock.remove(stock[i])


for i in pl:
    if i == [6,6]:
        sn.append(i)
        pl.remove(i)
        status = "computer"
        k = 2

for i in com:
    if i == [6,6]:
        sn.append(i)
        com.remove(i)
        status = "player"
        k =2

if k != 2:
    for i in pl:
        if i == [5,5]:
            sn.append(i)
            pl.remove(i)
            status = "computer"

    for i in com:
        if i == [5,5]:
            sn.append(i)
            com.remove(i)
            status = "player"





print('Stock:', stock)
print('Player:', pl)
print('Computer:', com)
print('snake', sn)
print('status:',status)
print('\n','============================================================================================','\n')
print('Stock size = ',len(stock))
print('Computer pieces = ',len(com))
print('\n',sn,'\n')
print('Your pieces:')
for i, z in enumerate(pl,start = 0):
  print('\n',i+1,pl[i])
if status == 'computer':
  print('\n','Status: Computer is about to make a move.')
else:
  print('\n','Status: It`s your tur to make move. Enter your command.')










