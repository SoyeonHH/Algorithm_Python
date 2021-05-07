num = list(range(1, 10001))

for i in range(0, 10000):
    d = i
    for j in range(len(str(i))):
        d = d + int(str(i)[j])
    if d in num:
        num.remove(d)

for n in num:
    print(n)