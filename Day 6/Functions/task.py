# def my_function():
#     print("Hello")
#     print("Bye")
#
# my_function()

def jump_over_wall():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


while not at_goal():
    if wall_in_front():
        jump_over_wall()
    else:
        move()