from turtle import *
from random import randint

# forward(100)#forward() indicate how many steps the turtle should move.
# shape('turtle')#shape() change the shape of the default arrow into other shapes, like a circle, a square, or an arrow.
# rt(90)#rigth() or rt() turn rigth x degrees before execute a move
# forward(200)

# def square():
#     a = 4
#     degrees = rt(360/4)
#     move = forward(100)
#     move_square = (move + degrees)*4
#     return
# square()

# # shape('circle')
# # forward(100)
# # right(90)
# # forward(100)
# # right(90)
# # forward(100)
# # right(90)
# # forward(100)

# for i in range(1,5):
#     print(i)

# def square():
#     for i in range(4):
#         forward(100)
#         rt(90)
# square()

# def circle_square():
#     for i in range(60):
#         for i in range(4):
#             speed(10)
#             shape('turtle')
#             forward(100)
#             rt(90)
#         right(5)
#     time.sleep(10)
# circle_square()

# def triangle():
#     for i in range(3):
#         speed(5)
#         shape('triangle')
#         rt(60)
#         forward(50)
#         rt(60)    
#     time.sleep(5)
# triangle()  

# def polygon(side, length):
#     for i in range (length):
#         shape('turtle')
#         forward(side)
#         rt(360/length)

# def spiral_square():
#     increase = 100
#     for i in range(60):
#         increase += 5
#         for i in range(4):
#             forward(increase)
#             rt(90)            
#         speed(10) 
#         hideturtle()   
#         rt(5)
# spiral_square()

# def spiral_star():
#     increase = 50
#     for i in range(60):
#         increase +=5
#         for i in range(5):
#             forward(increase)
#             right(144)
#         hideturtle()
#         speed(10)
#         rt(5)
# spiral_star()

# increase = 50
# for i in range(10):
#     increase +=5
#     print(increase)

speed(100)
def wander():
    while True:
        fd(3)
        if xcor() >= 200 or xcor() <= -200 or ycor() <= -200 or ycor() >= 200:
            lt(randint(90,180))
wander()