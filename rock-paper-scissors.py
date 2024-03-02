import random

count = 0
countPC = 0
while True:
    choices = ["rock","paper","scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper, or scissors?: ").lower()

    if player == computer:
        print("Computer: ",computer)
        print("Player: ",player)
        print("Tie!")
        print("Your Score: ",count)
        print("Computer Score: ",countPC)

    elif player == "rock":
        if computer == "paper":
            countPC = countPC + 1
            print("Computer: ",computer)
            print("Player: ",player)
            print("You Lose!")
            print("Your Score: ",count)
            print("Computer Score: ",countPC)

        if computer == "scissors":
            count = count + 1
            print("Computer: ",computer)
            print("Player: ",player)
            print("You Win!")
            print("Your Score: ",count)
            print("Computer Score: ",countPC)
            

    elif player == "scissors":
        if computer == "rock":
            countPC = countPC + 1
            print("Computer: ",computer)
            print("Player: ",player)
            print("You Lose!")
            print("Your Score: ",count)
            print("Computer Score: ",countPC)

        if computer == "paper":
            count = count + 1
            print("Computer: ",computer)
            print("Player: ",player)
            print("You Win!")
            print("Your Score: ",count)
            print("Computer Score: ",countPC)

    elif player == "paper":
        if computer == "scissors":
            countPC = countPC + 1
            print("Computer: ",computer)
            print("Player: ",player)
            print("Your Score: ",count)
            print("Computer Score: ",countPC)

        if computer == "rock":
            count = count + 1
            print("Computer: ",computer)
            print("Player: ",player)
            print("You Win!")
            print("Your Score: ",count)
            print("Computer Score: ",countPC)

    play_again = input("Play Again? (Yes/No): ").lower()

    if play_again != "yes":
        break
