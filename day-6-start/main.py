# program bot for make square
def move_right():
    turn_left()
    turn_left()
    turn_left()
turn_left()
move()
move_right()
move()
move_right()
move()
move_right()
move()



# program 2 jump the bot
def move_dir():
    turn_left()
    turn_left()
def jump1():
    move()
    turn_left()
def move_right():
    turn_left()
    turn_left()
    turn_left()
    
def win_game():
    jump1()
    jump1()
    move_dir()
    jump1()
    move_dir()
    jump1()

for step in range(0,6):
    win_game()