S=input().upper()
counting=[]
if len(list(set(S)))==1:
    print(*set(S))
else:
    for i in list(set(S)):
        counting.append([i,S.count(i)])
    counting.sort(key=lambda x:x[1])
    if counting[-1][1]==counting[-2][1]:
        print("?")
    else:
        print(counting[-1][0])