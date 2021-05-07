A,B=input().split()
A_="".join(reversed(A))
B_="".join(reversed(B))
print(A_) if int(A_)>int(B_) else print(B_)