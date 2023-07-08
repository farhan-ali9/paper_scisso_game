import random

game = ("rock", "paper", "scissor")
player = None
while True:
    print("--------------------Welcome to the Rock scissor paper--------------------")
    computer_choice = random.choice(game)
    player = input("Enter your choice : ")
    if player == computer_choice:
        print("Its tie")
    elif player == "rock" and computer_choice == "scissor":
        print("You win! Well played")
    elif player == "paper" and computer_choice == "scissor":
        print("You win! Well played")
    else:
        print("Computer win! Hard luck")
    user_continue = input("do you want to continue further (Y/N)")
    if user_continue.lower != 'y':
        continue
