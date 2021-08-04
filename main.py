
# SNAKE,WATER,GUN GAME
 
# snake will kill water
# water will kill gun
# gun will kill snake
 

import random
def gameWin(comp, you):
    # if two values are equal declare a tie
    if comp == you:
        return None
        
## check all possibilities when computer choose 'snake'
    elif comp == 'snake':
        if you =='water':
            return False
        elif you == 'gun':
            return True
## check all possibilities when computer choose 'water'
    elif comp == 'water':
        if you == 'gun':
            return True
        elif you == 'snake':
            return True
## check all possiblilities when computer choose 'gun'
    elif comp == 'gun':
        if you == 'snake':
            return False
        elif you == 'water':
            return True
print("Comp Turn: Snake(snake) Water(water) or Gun(gun)?")
randNo = random.randint(1,3)
if randNo == 1:
    comp = 'snake'
elif randNo == 2:
    comp = 'water'
elif randNo == 3:
    comp = 'gun'
you = input("Your Turn: Snake(snake) Water(water) or Gun(gun)?")
a = gameWin(comp, you)
print(f"Computer chose {comp}")
print(f"You chose {you}")
if a == None:
    print("The game is a tie!")
elif a:
    print("You win!")
else: 
    print("You lose!")
