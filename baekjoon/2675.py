T=int(input())
for t in range(T):
    S = input().split()
    for s in S[1]:
        print(s*int(S[0]),end='')
    print()