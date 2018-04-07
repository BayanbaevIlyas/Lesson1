a = []
for i in range(6):
    n = int(input())
    if n%2 == 0:
        a.insert(0,n)
    else:
        a.append(n)
print(a)
