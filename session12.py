# import turtle
# def draw_axis(sign):
#     for i in range(5):
#         if i == 0:
#             my_turtle.write(f"{i}", font=("arial", 14), align="left")
#         else:
#             my_turtle.write(f"{sign}{i}", font=("arial", 14), align="left")
#         my_turtle.forward(50)

# def draw_axis_wrapper(sign=""):
#     draw_axis(sign)
#     my_turtle.stamp()
#     my_turtle.home()
    
# root = turtle.Screen()
# my_turtle = turtle.Turtle()
# my_turtle.speed("fastest")
# draw_axis_wrapper()
# my_turtle.left(90)
# draw_axis_wrapper()
# my_turtle.left(180)
# draw_axis_wrapper("-")
# my_turtle.right(90)
# draw_axis_wrapper("-")
# my_turtle.ht()

# turtle.done()


# a = [1,2,3]
# print(sum(a))

# def mysum(numbers):
#     res = 0
#     i = 0
#     while i < len(numbers):
#         res += numbers[i]
#         i += 1
#     return res
# print(mysum(a))