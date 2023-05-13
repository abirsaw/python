def hurdle():
    turn_left()
    turn_left()
    turn_left()
    move()
def ro():   
    move()
    turn_left()
    move()
    hurdle()
    hurdle()
    turn_left()
while at_goal() != True:
    ro()
