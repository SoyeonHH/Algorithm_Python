'''
출 처 : Python 계단밟기, wikidocs, https://wikidocs.net/20396
설 명 : tirtle 갖고 놀면서 프로그래밍이랑 친해지자~
'''

# 거북이를 사용하자
import turtle
turtle.title('거북아놀자')
turtle.color('black','red')
turtle.shape('turtle')

# 함수 정의
def move(length):
    turtle.penup() # 위로 그리기/이동하기
    turtle.forward(length)
    turtle.pendown()

move(-200) # 함수 호출
# 사각형 그리기
for _ in range(4):
    turtle.fd(50)
    turtle.lt(90)

move(100)
# 도장 찍기
colors = ['red','green','yellow','blue']
for color in colors:
    turtle.color('black',color)
    turtle.fd(50)
    turtle.stamp()

move(150)
# 삼각형 그리기
for i in range(3):
    turtle.lt(120)
    turtle.color('black', colors[i])
    turtle.fd(100)
    turtle.stamp()


# 클릭 시 종료
turtle.exitonclick()