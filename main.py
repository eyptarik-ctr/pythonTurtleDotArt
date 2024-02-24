from turtle import*
from random import*
x_cordinats = [-80 ,-70 ,-60 ,-50 ,-40 ,-30 ,-20 ,-10 ,0 ,10 ,20 ,30 ,40 ,50 ,60 ,70 ,80]
y_cordinats = [-80 ,-70 ,-60 ,-50 ,-40 ,-30 ,-20 ,-10 ,0 ,10 ,20 ,30 ,40 ,50 ,60 ,70 ,80]
colors = ['#ef233c','#c1121f','#780000','#003049','#669bbc','#2a9d8f','#283618','#e76f51','#3a86ff','#2b2d42','#43aa8b','#03045e','#ffd60a','#b8c0ff','#14213d','#7400b8','#a7c957','#778da9','#22577a','#52796f','#ff477e','#720026','#00bbf9','#38b000','#006400']
pen = Turtle()
pen.penup()
pen.speed('fastest')
pen.pensize(35)
pen.hideturtle()
for x in x_cordinats:
    for y in y_cordinats:
        pen.setx(x*7)
        pen.sety(y*6)
        pen.pendown()
        pen.dot(38,choice(colors))
        pen.penup()

drawingBoard = Screen()
drawingBoard.bgcolor('#ffecd1')
drawingBoard.mainloop()