from random import randint

print("Rock...")
print("Paper...")
print("Scissors...")

playerwins = 0
computerwins = 0
while playerwins < 2 and computerwins < 2:
    randomint = randint(0, 2)
    options = ["rock", "paper", "scissors"]
    computer = options[randomint]
    player = input("Player, make your move: ").lower()
    print(f"computer played {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock":
        if computer == "scissors":
            print("player wins!")
            playerwins += 1
        elif computer == "paper":
            print("computer wins!")
            computerwins += 1
    elif player == "paper":
        if computer == "rock":
            print("player wins!")
            playerwins += 1
        elif computer == "scissors":
            print("computer wins!")
            computerwins += 1
    elif player == "scissors":
        if computer == "paper":
            print("player wins!")
            playerwins += 1
        elif computer == "rock":
            print("computer wins!")
            computerwins += 1
    else:
        print("something went wrong")

print(f'the game has ended. The computer has {computerwins} points and \
      the player has {playerwins} points')
