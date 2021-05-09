logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]

letters, digits = [], []
for log in logs:
    if log.split()[1].isdigit() == 0:
        letters.append(log)
    else:
        digits.append(log)

# 람다 표현식 이용하여 letters 재정렬 (2개의 key 이용)
letters.sort(key=lambda x:(x.split()[1:], x.split()[0]))
print(letters + digits)
