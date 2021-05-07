T = int(input())

for t in range(T):
    A,B = map(int, input().split())
    print("Case #" + str(t+1) + ": " + str(A) + " + " + str(B) + " = " + str(A+B))