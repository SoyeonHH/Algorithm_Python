import collections
strs = ["eat","tea","tan","ate","nat","bat"]

# KeyError 방지 위한 선언 (딕셔너리에 키 값 입력하여 바로 append() 적용하기 위함)
anagrams = collections.defaultdict(list)

for word in strs:
    # 정렬하여 딕셔너리에 추가 (sorted()는 정렬하여 리스트를 반환)
    anagrams[''.join(sorted(word))].append(word)
print(list(anagrams.values()))