def binary(a):
    for i in range(1,100):
        b.append(cube(i))
    l = 0
    r  = len(b)
    while r > l + 2:
        m = (l + r) // 2
        if a < b[m]:
            r = m
        else:
            l = m
    return  l+1


def cube(x):
    v = x**3
    return v

b = []
a = int(input())
print(binary(a))