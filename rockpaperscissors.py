import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ___)___
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ___)___
          ______)
       __________)
      (____)
---.__(___)
'''

game_image=[rock,paper,scissors]
choice = int(input("ENTER YOUR CHOICE '0 FOR ROCK, 1 FOR PAPER , 2 FOR SCISSORS'")) 
print(game_image[choice])

comp_choice=random.randint(0,2)
print(game_image[comp_choice])

if choice >=3 or choice <0:
    print("Your choice is invalid")
elif choice=='0' and comp_choice=='2':
    print("you win")
elif choice=='0' and comp_choice=='2':
    print("you lose")
elif choice > comp_choice:
    print("You win")
elif comp_choice > choice:
    print("You lose")
elif choice==comp_choice:
    print("Match Draw")
else:
    print("You are a loser")

