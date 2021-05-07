N = int(input())
for i in range(N):
    result = str(input())
    score=0
    acculm=0
    for j in range(len(result)):
        if result[j]=='O':
            acculm+=1
            score=score+acculm
        else:
            acculm=0
    print(score)