nums=[]
while True:
    try:
        nums.append(int(input())%42)
    except:
        break
print(len(list(set(nums))))