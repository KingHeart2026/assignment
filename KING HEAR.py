import random
name = input("What is you name   ")
print("WELCOME TO KING HEART GAME🤷‍♀️👏 "  +  name)
player = input('choose the one of your choice🕙😈 rock,paper or scissors: ')
choices = ["rock", "paper","scissors"]

computer = random.choice(choices)
print("computer chose:  ",computer)

if player == "paper" and computer == "rock":
     print("YOU WON👏")
elif player == "rock" and computer == "scissors":
          print("YOU WON👏")
elif player == "scissors" and computer == "paper":
        print("YOU WON👏")
elif player == "paper" and computer == "rock":
      print ("YOU WON👏") 
elif player == computer:
    print("DRAW🤷‍♀️")
else:
      print("YOU FAILED😫")     

