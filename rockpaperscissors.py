import random
from banner import banner

def print_welcome_message():
    print("We are going to play Rock, Paper, Scissors. The first to win 2 rounds out of 3 rounds is the winner")

def get_players_choice():
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    choice = int(input("What is your choice? "))
    return choice

def scoreboard(player, cpu):
    print(f"Score: Player: {player} Computer: {cpu} ")


banner("ROCK, PAPER, SCISSORS", "Ciera")
print_welcome_message()
cpu_score = 0
players_score = 0
while cpu_score < 3 and players_score < 3:
    scoreboard(players_score, cpu_score)
    players_choice = get_players_choice()
    cpu_choice = random.randint(1,3)
    if players_choice == 1:
        if cpu_choice == 1:
            print("You both chose rock, it is a tie.")
        if cpu_choice == 2:
            print("Player chose rock, computer chose paper. You lose")
            cpu_score = cpu_score + 1
        if cpu_choice == 3:
            print("player chose rock, computer chose scissors, You win!")
            players_score = players_score + 1
    if players_choice == 2:
        if cpu_choice == 1:
            print("player chose paper, computer chose rock, You win!")
            players_score = players_score + 1
        if cpu_choice == 2:
            print("Its a tie, you both chose paper.")
        if cpu_choice == 3:
            print("player chose paper, computer chose scissors, you lose.")
            cpu_score = cpu_score + 1
    if players_choice == 3:
        if cpu_choice == 1:
            print("player chose scissors, computer chose rock, you lose")
            cpu_score = cpu_score + 1
        if cpu_choice == 2:
            print("player chose scissors, computer chose paper, you win!")
            player_score = players_score + 1
        if cpu_choice == 3:
            print("You both chose scissors, its a tie")
if cpu_score >= 3:
    print("Lose")
elif player_score >= 3:
    print("win")