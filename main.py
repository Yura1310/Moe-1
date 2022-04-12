b = list(input())
a = list(input())
q = []
w = []
e = []
for i in b:
  q.append(i)
for i in a:
  w.append(i)
print(w,q)
for z, x in zip(q, w):
  e.append(z)
  e.append(x)
f = ''.join(e)
print(f)