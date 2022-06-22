import random

def play():
    user = input ("\nWhat's your choice? 'r' for Rock, 'p' for Paper ,'s' for Scissors?").lower()
    computer = random.choice(['r' , 'p' , 's'])

    if user == computer:
        return "It\'s a tie!"

    if winner(user, computer):
        return "You Won!"

    return "You Lost!"

def winner(player, opponent):
    #return true if player wins
    # r > s , s > p , p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
    or (player == 'p' and opponent == 'r'):
        return True

i = int(input("How many times do you want to play?"))
while i != 0:
    print(play())
    i -= 1
