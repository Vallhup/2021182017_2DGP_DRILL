import turtle

turtle.reset()

# 가로줄 그리기
y = 0

while y <= 500:
    turtle.penup()
    turtle.goto(0, y)
    turtle.pendown()
    turtle.goto(500, y)
    y += 100

# 세로줄 그리기
x = 0

while x <= 500:
    turtle.penup()
    turtle.goto(x, 0)
    turtle.pendown()
    turtle.goto(x, 500)
    x += 100