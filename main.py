import random
stock = [[i, j] for i in range(7) for j in range(i, 7)]
pl = []
com = []
k = 0
sn = []
status = ('player','computer')
while True:
  random.shuffle(stock, random.random)
  for i in range(1):
      if stock[i] == [6, 6] or [5, 5]:
          k=1
  if k == 1:
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






