#ROCK PAPER Scissors Game
import random

computer = random.choice(["rock","paper","scissors"])

while True:
    user = input("please pick rock paper or scissors : \n")
    print(computer)

    if user == computer:
        print("Draw play again")
    elif user == "rock" and computer == "scissors":
        print("user wins")
    elif user == "paper" and computer == "rock":
        print("user wins")
    elif user == "scissors" and computer == "paper":
        print("user wins")
    elif computer == "rock" and user == "scissors":
        print("computer wins")
    elif computer == "paper" and user == "rock":
        print("computer wins")
    elif computer == "scissors" and user == "paper":
        print("user wins")

    if user == "quit":
        break











