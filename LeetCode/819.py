import collections
import re

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

# Solution
# --------------------------------------------------------------

# 입력값 전처리
words = [word for word in re.sub(r'[^\w]',' ', paragraph)
    .lower().split()
         if word not in banned]

# 빈도수가 가장 높은 요소 반환
counts = collections.Counter(words)     # return [('word',count), ...]
print(counts.most_common(1)[0][0])   # most_common(1) : 가장 빈번한 counter collection 1개 반환