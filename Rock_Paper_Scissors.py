import random

def play():
    user = input('Enter "R" for Rock, "P" for Paper, "S" for Scissor : '  ).lower()
    computer = random.choice(['r', 'p', 's'])
    print(f'computer is {computer}')
    if user == computer:
        return '********* tied *********'
    elif winner(computer, user):
        return '********* you won *********'
    else:
        return '********* you lost *********'

def winner(side1,side2):
    # p < s, s < r, r < p
    if (side1 == 'p' and side2 == 's') or (side1 == 's' and side2 == 'r') or (side1 == 'r' and side2 == 'p'):
        return True


print('########## Rock Paper Scissors ##########')
p = input('Do you wanna play? (y/n) : ').lower()
if p == 'y':
    print(play())
elif p == 'n':
    exit()

