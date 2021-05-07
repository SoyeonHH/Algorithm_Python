C = int(input())
for i in range(C):
    case = list(map(int,input().split()))
    avrg = sum(case[1:])/case[0]
    over_num=0
    for j in case[1:]:
        if j>avrg:
            over_num+=1
    print("{:0.3f}".format(100*over_num/case[0]) + "%")