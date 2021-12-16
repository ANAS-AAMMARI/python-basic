import random

user_wins = 0
computer_wins = 0

computer_choose = ["rock", "paper", "scissor"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    computer_input = random.choice(computer_choose)
    if user_input in computer_choose or user_input == "q":
        if user_input == "rock" and computer_input == computer_choose[2]:
            user_wins += 1
            print("you win :D")
        elif user_input == computer_choose[1] and not computer_input != computer_choose[0]:
            user_wins += 1
            print("you won :D")
        elif user_input == computer_choose[2] and computer_input == computer_choose[1]:
            user_wins += 1
            print("you won :D")
        elif computer_input == user_input:
            print("equal")
        elif user_input == "q":
            print("computer wins :", computer_wins)
            print("your wins :", user_wins)
            quit()
        else:
            computer_wins += 1
            print("computer win :(")
    else:
        print("type something valid")
        continue

