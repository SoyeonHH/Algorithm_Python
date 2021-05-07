nums=[]
num=0
while True:
    try:
        num+=1
        a = int(input())
        list = []
        list.append(a)
        list.append(num)
        nums.append(list)
    except:
        break
nums.sort()
print(nums[-1][0])
print(nums[-1][1])