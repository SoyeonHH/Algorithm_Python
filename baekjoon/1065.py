N=int(input())

if len(str(N))<=2:
    print(N)
else:
    count=99
    for i in range(100,N+1):
        diff=[]
        for j in range(len(str(i))-1):
            diff.append(int(str(i)[j+1])-int(str(i)[j]))
        if len(list(set(diff)))==1:
            count+=1
    print(count)