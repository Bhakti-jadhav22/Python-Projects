#Stone Paper Cissor game
''' 
'1' is for Stone
'-1' is for Paper
'0' is for Scissor
'''

import random
string = input("Enter your choice: ")
yourmove = string.capitalize()
dictionary = {"Stone": 1, "Paper":-1, "Scissor": 0}
reversedict = {1: "Stone", -1: "Paper", 0: "Scissor"}

computermove = random.choice([1,-1,0])
print(f"Computer move is {reversedict[computermove]}\nYour move is {yourmove}")

if(computermove == dictionary[yourmove]):
    print("Tie")
else:
    if(computermove == 1 and dictionary[yourmove] == -1): 
        print("You Win!")
    elif(computermove == 1 and dictionary[yourmove] == 0): 
        print("You Lose!")
    elif(computermove == -1 and dictionary[yourmove] == 1): 
        print("You Lose!")
    elif(computermove == -1 and dictionary[yourmove] == 0):
        print("You Win!")
    elif(computermove == 0 and dictionary[yourmove] == 1):
        print("You Win!")
    elif(computermove == 0 and dictionary[yourmove] == -1):
        print("You Lose!")

