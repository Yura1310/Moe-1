import random
stock = [[i, j] for i in range(7) for j in range(i, 7)]
pl = []
com = []
k = 0
sn = []
status = ['player','computer']
# for i in range(7):
#     domino.append([0,i])
# for i in range (6):
#     domino.append([1, i+1])
# for i in range (5):
#     domino.append([2, i+2])
# for i in range (4):
#     domino.append([3, i+3])
# for i in range(3):
#     domino.append([4, i+4])
# for i in range(2):
#     domino.append([5, i+5])
# for i in range(1):
#     domino.append([6, i+6])

while True:
    random.shuffle(stock, random.random)
    for i in range(14):
        if stock[i] == [6, 6] or [5, 5]:
            k=1
    if k ==1:
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
        print('status:',status[0])
        k = 2

for i in com:
    if i == [6,6]:
        sn.append(i)
        com.remove(i)
        print('status:',status[1])
        k =2

if k != 2:
    for i in pl:
        if i == [5,5]:
            sn.append(i)
            pl.remove(i)
            print('status:',status[0])

    for i in com:
        if i == [5,5]:
            sn.append(i)
            com.remove(i)
            print('status:',status[1])


print('Stock:', stock)
print('Player:', pl)
print('Computer:', com)
print('snake', sn)







