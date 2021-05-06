'''
출 처 : Python 계단밟기, wikidocs, https://wikidocs.net/20403
주 제 : 파이썬 표준 출력
'''

# 형식에 맞추어 출력하기
print('나의 이름은 {}입니다'.format('soyeon'))
print('나의 이름은 "{0}입니다. 나이는 {1}세이고 성별은 {2}입니다.'.format('soyeon',24,'여성'))
print('나이:{1}세, 성별:{2}, 이름:{0}'.format('soyeon',24,'여성'))
print('나이:{age}세, 성별:{gender}, 이름:{name}'.format(name='soyeon', age=24, gender='여성'))
print('-' * 40)

# 문자열 앞 0으로 채우기 zfill()
print('12'.zfill(5))  # 00012
print('-12'.zfill(5))  # -0012
print('3.141'.zfill(7))  # 003.141
print('-3.141'.zfill(7))  # -03.141
print('3.14159265359'.zfill(5))  # 3.14159265359
print('-3.14159265359'.zfill(5))  # -3.14159265359
print('문자열'.zfill(10))  # 0000000문자열
print('문자열'.zfill(1))  # 문자열
print('-' * 40)

# 길이와 정렬
print('Python is [{:15}]'.format('good'))  # Python is [good           ]
print('Python is [{:<15}]'.format('good'))  # Python is [good           ]
print('Python is [{:>15}]'.format('good'))  # Python is [           good]
print('Python is [{:^15}]'.format('good'))  # Python is [     good      ]
print('-' * 40)

# 채움 문자
# {[인덱스]:[채움문자][정렬][길이][,|_][형식문자]
print('[{0:★<5d}] [{1:★<5d}] [{2:★<5d}]'.format(1,-2,3))  # [1★★★★] [-2★★★] [3★★★★]

# 숫자 표시 형식
print('[{0:>5,}] [{1:>5,}] [{2:>5,}]'.format(11544435,-2544254,35454343)) # , : 천단위 마다 콤마를 붙여줍니다.
print('[{0:>5_}] [{1:>5_}] [{2:>5_}]'.format(11544435,-2544254,35454343))  # _ : 천단위 마다 밑줄을 붙여줍니다.
print('[{0:>5e}] [{1:>5e}] [{2:>5e}]'.format(11544435,-2544254,35454343))  # e : 숫자를 지수 형식으로 만들어 줍니다.
print('[{0:=05d}] [{1:=05d}] [{2:=05d}]'.format(1,-2,3))  # = : 숫자 형식에만 사용합니다. 부호를 항상 제일 앞에 출력합니다.

print('-' * 40)

# 진법
# {[인덱스]:[전체자릿수][.소수이하자릿수]}
print('[{0:5b}] [{1:5b}] [{2:5b}]'.format(11,-22,33))    # 2진수(b)
print('[{0:5o}] [{1:5o}] [{2:5o}]'.format(11,-22,33))    # 8진수(o)
print('[{0:5x}] [{1:5x}] [{2:5x}]'.format(11,-22,33))    # 16진수 소문자(x)
print('[{0:5X}] [{1:5X}] [{2:5X}]'.format(11,-22,33))    # 16진수 대문자(X)
print('-' * 40)

# 실수 출력 형식 지정
import math
print('{0:.3f}'.format(math.pi))  # 3.142
print('{0:0.7f}'.format(math.pi))  # 3.1415927
print('{0:10.3f}'.format(math.pi))  #      3.142
print('{0:20.7f}'.format(math.pi))  #            3.1415927
print('-' * 40)

# {}는 세 번 입력, %는 두 번 입력
print('{{{0}}}씨는 상위 {{{1}}}%안에 있는 사람입니다.'.format('soyeon',10))  # {soyeon}씨는 상위 {10}%안에 있는 사람입니다.
print('%s씨는 상위 %d%%안에 있는 사람입니다.'%('soyeon',10))  # soyeon씨는 상위 10%안에 있는 사람입니다.
print('-' * 40)