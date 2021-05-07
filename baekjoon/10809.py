S=input()
indexing=[]
for i in list(range(97,123)):
    indexing.append(S.find(chr(i)))
print(*indexing)