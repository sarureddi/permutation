m1 = int(input())
a1 = list(map(int,input().split()))
c1,l1 = 0,[]
b1 = [x1 for x1 in range(1,m1+1)]
for i1 in a1:
  if i1 in b1:
    b1.remove(i1)
k1 = 0
for i1 in range(0,m1-1):
  p1 = a1[i1]
  for j1 in range(i1+1,m1):
    if p1 == a1[j1]:
      if p1 < b1[k1]:
        a1[j1] = b1[k1]
        c1 += 1
      else:
        a1[i1] = b1[k1]
        c1 += 1
      k1 += 1
print(c1)
print(*a1)
