N = int(input())
score = list(map(int, input().split()))
score.sort()
new_score=[]
for i in range(N):
    new_score.append(100*score[i]/score[-1])
print(sum(new_score)/len(new_score))