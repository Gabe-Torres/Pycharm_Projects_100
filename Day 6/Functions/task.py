def my_function():
    print("Hello")
    print("Bye")

my_function()

def jump_over_wall():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()


def turn_right():
    turn_left()
    turn_left()
    turn_left()

while front_is_goal():
    move()
turn_left()

while not at_goal():
    if wall_in_front():
        jump_over_wall()
    else:
        move()

 while not at_goal():
     if right_is_clear():
         turn_right()
         move()
     elif front_is_clear():
         move()
     else:
         turn_left()