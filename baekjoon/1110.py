N = int(input())
N = "0" + str(N) if N < 10 else str(N)
origin = N
cycle = 0

while True:
    add_N = int(N[0]) + int(N[1])
    N = 10 * int(N[1]) + (add_N % 10)
    N = "0" + str(N) if N < 10 else str(N)
    cycle += 1
    if N == origin:
        break

print(cycle)