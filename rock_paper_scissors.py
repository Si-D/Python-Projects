import random

choices = ["Rock", "Paper", "Scissors"]
computer = random.choice(choices)
cpu_score = 0
player_score = 0
while True:
    player = input("Rock, paper or scissors?").capitalize()

    if player == computer:
        print("It is a tie")
    elif player == "Rock":
        if computer == "Paper":
            print("Computer wins")
            cpu_score+=1
        else:
            print("You win")
            player_score+=1
    elif player == "Paper":
        if computer == "Scissors":
            print("Computer wins")
            cpu_score+=1
        else:
            print("You win!")
            player_score+=1
    elif player == "Scissors":
        if computer == "Rock":
            print("Computer Wins")
            cpu_score+=1
        else:
            print("You win!")
            player_score+=1
    elif player == 'E':
        print("Final Score:")
        print("Cpu Score:", cpu_score)
        print("Player Score:", player_score)
        if player_score > cpu_score:
            print("You have Won with a total of {} rounds".format(player_score))
        elif player_score == cpu_score:
            print("It's a tie with both having won {} rounds".format(player_score))
        else:
            print("The computer has won with a total of {} rounds".format(cpu_score))
        break
    else:
        print("Invalid input!")