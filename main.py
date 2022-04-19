import random

level = int(input('Choose level: 1 - ez, 2 medium, 3 - hard: '))
stock = [[i, j] for i in range(7) for j in range(i, 7)]
pl = []
com = []
k = 0
sn = []
status = ('player', 'computer')
t = 0
sc = 0
while True:
    if t >= 1:
        break
    random.shuffle(stock, random.random)
    for i in range(14):
        if stock[i] == [6, 6]:
            t += 1
        if stock[i] == [5, 5]:
            t += 1

for i in range(7):
    pl.append(stock[i])
    stock.remove(stock[i])

for i in range(7):
    com.append(stock[i])
    stock.remove(stock[i])

for i in pl:
    if i == [6, 6]:
        sn.append(i)
        pl.remove(i)
        status = "computer"
        yyy = 1
        k = 2

for i in com:
    if i == [6, 6]:
        sn.append(i)
        com.remove(i)
        status = "player"
        yyy = 2
        k = 2

if k != 2:
    for i in pl:
        if i == [5, 5]:
            sn.append(i)
            pl.remove(i)
            status = "computer"
            yyy = 1

    for i in com:
        if i == [5, 5]:
            sn.append(i)
            com.remove(i)
            status = "player"
            yyy = 2

print('Stock:', *stock)
print('Player:', *pl)
print('Computer:', *com)
print('snake', *sn)
print('status:', status)
print('\n', '============================================================================================', '\n')
print('Stock size = ', len(stock))
print('Computer pieces = ', len(com))
print('\n', *sn, '\n')
print('Your pieces:')
for i, z in enumerate(pl, start=0):
    print('\n', i + 1, pl[i])
h = 0


def com_f(com, negcc):
    for i in range(len(com)):
        a = com[i]
        e = sn[len(sn) - 1]
        y = sn[0]
        if a[0] == e[1]:
            sn.append(com[i])
            com.pop(i)
            negcc.pop(i)
            # if len(sn) != 2:
            #     sn.pop(len(sn)-2)
            #     sn.insert(len(sn) - 1, [])
            return sn
            break
        elif a[1] == e[1]:
            sn.append(negcc[i])
            com.pop(i)
            negcc.pop(i)
            # if len(sn) != 2:
            #     sn.pop(len(sn)-2)
            #     sn.insert(len(sn) - 1, [])
            return sn
            break
        elif a[0] == y[0]:
            sn.insert(0, negcc[i])
            com.pop(i)
            negcc.pop(i)
            # if len(sn) != 2:
            #     sn.pop(1)
            #     sn.insert(1, [])
            return sn
            break
        elif a[1] == y[0]:
            sn.insert(0, com[i])
            com.pop(i)
            negcc.pop(i)
            # if len(sn) != 2:
            #     sn.pop(1)
            #     sn.insert(1, [])
            return sn
            break

        if i == len(com) - 1:
            if len(stock) == 0:
                print('stock empty, computer skip')
                return (sn)
            print('Computer take pieces')
            com.append(stock[0])
            negcc.append(sorted(stock[0], reverse=True))
            stock.pop(0)
            print('Stock size:', len(stock))
            return sn


def pl_f(q, pl, negpc):
    global kk
    h = len(pl)
    kk = 0
    for i in range(len(pl)):
        b = pl[i]
        e = sn[len(sn) - 1]
        y = sn[0]

        if q < 0:
            if b[0] == y[0]:
                if q == -(i + 1):
                    sn.insert(0, negpc[i])
                    pl.pop(i)
                    negpc.pop(i)
                    # if len(sn) != 2:
                    #     sn.pop(1)
                    #     sn.insert(1, [])
                    return sn
                    break
            elif b[1] == y[0]:
                if q == -(i + 1):
                    sn.insert(0, pl[i])
                    pl.pop(i)
                    negpc.pop(i)
                    # if len(sn) != 2:
                    #     sn.pop(1)
                    #     sn.insert(1, [])
                    return sn
                    break
        elif q > 0:
            if b[1] == e[1]:
                if q == i + 1:
                    sn.append(negpc[i])
                    pl.pop(i)
                    negpc.pop(i)
                    # if len(sn) != 2:
                    #     sn.pop(len(sn)-2)
                    #     sn.insert(len(sn)-1, [])
                    return sn
                    break
            elif b[0] == e[1]:
                if q == i + 1:
                    sn.append(pl[i])
                    pl.pop(i)
                    negpc.pop(i)
                    # if len(sn) != 2:
                    #     sn.pop(len(sn)-2)
                    #     sn.insert(len(sn)-1, [])
                    return sn
                    break
    if h == len(pl):
        # if len(stock) == 0:
        #     break
        print('your number cannot be put, repeat')
        kk += 1
        return sn
    return sn


negpc = [];
negcc = []
for i in range(len(pl)): c = sorted(pl[i], reverse=True);    negpc.append(c)
# print(negpc)
for i in range(len(com)): c = sorted(com[i], reverse=True);  negcc.append(c)
# print(negcc)


while True:
    if status == 'computer':
        print('\n', 'Status: Computer is about to make a move.')
        o = input('Press Enter:')
        if o == '':
            print('\n', 'Snake:', *com_f(com, negcc))
            status = 'player'

            for w, z in enumerate(pl, start=0):
                print(w + 1, pl[w])
    if status == 'player':
        while True:
            try:
                q = int(input('Number:'))
                if abs(q) > len(pl):
                    print('ancorrect, repeat')
                else:
                    break
            except ValueError as err:
                print('V Error', 'repeat', err)
                continue

        if q == 0:
            if len(stock) == 0:
                print('stock empty')
            else:
                pl.append(stock[0])
                negpc.append(sorted(stock[0], reverse=True))
                stock.pop(0)
                print('Stock size:', len(stock))
                print('Snake:', *sn)
                status = 'computer'
        else:

            print('\n', 'Snake:', *pl_f(q, pl, negpc))
            for w, z in enumerate(pl, start=0):
                print(w + 1, pl[w])
            if kk > 0:
                status = 'player'
            if kk == 0:
                status = 'computer'

    if len(sn) > 10:
        sc = 0
        for i in sn:
            for j in range(2):
                if sn[len(sn) - 1][1] == i[j] and sn[0][0] == i[j]:
                    sc += 1
        if sc == 8:
            print('\n', 'The game is over. Draw!')
            break

    if len(pl) == 0:
        print('\n', 'The game is over. You won!', '\n', 'Computer pieces:', com)
        break
    if len(com) == 0:
        print('\n', 'The game is over. The computer won!')
        break
    if len(pl) == 0 and len(pl) == len(com) and yyy == 1:
        print('\n', 'The game is over. Draw!')
    elif len(pl) == 0 and len(pl) == len(com) and yyy == 2:
        print('\n', 'The game is over. Computer won!')