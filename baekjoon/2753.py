x = int(input())

answer = 0
if (x % 4) == 0:
    if ((x % 100) != 0) or ((x % 400) == 0):
        answer = 1

print(answer)