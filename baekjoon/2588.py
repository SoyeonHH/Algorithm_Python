a = int(input())
b = int(input())

b_1 = b%10
b_10 = (b//10)%10
b_100 = (b//100)

mid_1 = a*b_1
mid_2 = a*b_10
mid_3 = a*b_100

print(mid_1)
print(mid_2)
print(mid_3)
print(mid_1 + 10*mid_2 + 100*mid_3)