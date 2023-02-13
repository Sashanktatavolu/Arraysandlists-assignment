array = list(map(int,input().split()))
a = []
b = []
for i in array:
    if i not in a:
        a.append(i)
for i in a:
    if array.count(i) > 1:
        b.append(i)
print(*b,sep= ' ')



