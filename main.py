def binary(b):
    l = 0
    r = len(b)
    while r > l + 1:
        m = (l + r) // 2
        print(summ(b[m]),b[m])
        if k>summ(b[m]):
            r = m
        else:
            l = m
    return b[l]
def summ(x):
    v = 0
    for i in range (len(a)):
        v = v + (a[i]//x)
    return (v)
a = []
b = []
n, k = input().split()
n, k = int(n), int(k)
for i in range(n):
    a.append(int(input()))
for i in range(min(a)//k,sum(a)//k+1):
    b.append(i)
print(binary(b))
