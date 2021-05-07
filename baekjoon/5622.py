S=input()
second=0
for s in S:
    if s in "ABC":
        second+=3
    elif s in "DEF":
        second+=4
    elif s in "GHI":
        second+=5
    elif s in "JKL":
        second+=6
    elif s in "MNO":
        second+=7
    elif s in "PQRS":
        second+=8
    elif s in "TUV":
        second+=9
    elif s in "WXYZ":
        second+=10
    else:
        second+=11
print(second)