A = int(input())
B = int(input())
C = int(input())
N = A*B*C

for i in range(10):
    num=0
    for j in range(len(str(N))):
        if str(N)[j] == str(i):
            num+=1
    print(num)