'''
출 처 : Python 계단밟기, wikidocs, https://wikidocs.net/20369
설 명 : 행결합은 세미콜론(;), 행분리는 역슬래쉬(\) 또는 괄호
'''

# 행결합 : 세미콜론(;)
print("first row"); print("second row")
print("first row"); print("second row");

# 행분리 : 역슬래쉬(\), 괄호
a = 1 + 2 + 3 + \
    4 + 5 + 6
print(a)

b = (1 + 2 + 3 +
        4 + 5 + 6)
print(b)

# 파라미터를 넘기는 것이라면 comma 뒤에서 그냥 엔터를 쓰면 된다.
print("Hello", "Python",
        end="\n", sep="\t")

# 문자열 줄바꿈
print("아주 아주 긴 문자열이라고 가정하자"
    "앤터 치면 자동으로 ""가 열고닫히며 1줄로 인식한다.")