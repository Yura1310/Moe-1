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

def com_f (com,negcc):
    for i in range(len(com)):
        a = com[i]
        e = sn[len(sn) - 1]
        # print(a, e)
        if a[0] == e[1]:
            sn.append(com[i])
            com.pop(i)
            negcc.pop(i)
            return sn
            break
        elif a[1] == e[1]:
            sn.append(negcc[i])
            com.pop(i)
            negcc.pop(i)
            return sn
            break
        if i == len(com)-1:
            print('Computer take pieces')

            com.append(stock[0])
            negcc.append(sorted(stock[0],reverse=True))
            stock.pop(0)
            print('Stock size:',len(stock))
            return sn



def pl_f (q,pl,negpc):
    for i in range(len(pl)):
        b = pl[i]
        e = sn[len(sn)-1]
        # print(b,e)
        if b[1]  == e[1]:
            if q == i+1:
                sn.append(negpc[i])
                pl.pop(i)
                negpc.pop(i)
                return sn
                break
        if b[0]  == e[1]:
            if q == i+1:
                sn.append(pl[i])
                pl.pop(i)
                negpc.pop(i)
                return sn
                break



negpc = [];negcc = []
for i in range(len(pl)):c = sorted(pl[i],reverse = True);    negpc.append(c)
# print(negpc)
for i in range(len(com)):c = sorted(com[i],reverse = True);  negcc.append(c)
# print(negcc)


while True:
    if status == 'computer':
        o = input('Press Enter:')
        if o == '':
            print('\n', 'Status: Computer is about to make a move.')
            print('\n','Snake:',com_f(com,negcc))
            status = 'player'
    if status == 'player':
        while True:
            q = int(input('Number:'))
            if q <= len(pl):
                break
            else:
                print('ancorrect, repeat')
        if q == 0:
            pl.append(stock[0])
            negpc.append(sorted(stock[0],reverse=True))
            stock.pop(0)
            print('Stock size:',len(stock))
        print('\n','Snake:',pl_f(q,pl,negpc))
        for w, z in enumerate(pl, start=0):
            print( w + 1, pl[w])

        status = 'computer'
    if len(pl) == 0:
        print('\n', 'The game is over. You won!')
        break
    if len(com) == 0:
        print('\n', 'The game is over. The computer won!')
        break
    if len(stock)-1 == 0:
        if len(pl) < len(com):
            print('\n','The game is over. You won!')
            break
        elif len(pl) > len(com):
            print('\n','The game is over. The computer won! Computer pieces:',len(com))
            break

