# The game() function in a program lets a user play a game and returns the score
# as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or
# contains the previous Hi-score. You need to write a program to update the Hiscore whenever the game() function breaks the Hi-score.

import random

def game():
    print("you are playing the game!")
    score = random.randint(1, 62)
    # fetch the hiscore
    with open("File input and outputs\Practice Set\hiScore.txt") as f:
        hiScore = f.read()
        if(hiScore!=""):
            hiScore = int(hiScore)
        else:
            hiScore = 0
            
    print(f"your score: {score}")
    
    if(score>hiScore):
        with open("File input and outputs\Practice Set\hiScore.txt", "w") as f:
           f.write(str(score))
    
    
    return score
game()
