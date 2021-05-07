nums=[]
while True:
    try:
        num = int(input())
        nums.append(num)
    except:
        break
print(max(nums))
print(nums.index(max(nums))+1)