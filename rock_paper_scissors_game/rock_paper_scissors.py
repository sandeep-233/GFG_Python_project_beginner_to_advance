import random

# print instruction
print("Winning rules of the game ROCK PAPER SCISSORS are: \n"
       + "Rock vs Paper -> Paper wins \n" 
       + "Rock vs Scissors -> Rock wins \n" 
       + "Paper vs Scissors -> Scissors wins \n")

while (True):
    print("Enter your Chioce \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")

    # take the user input 
    choice = int(input("Enter your choice: "))

    # looping util user enters valid input 
    while (choice > 3 or choice < 1):
        choice = int(input("Enter a valid choice please: "))
    
    # initialize value of choice_name variable corresponding to the choice value 
    if(choice == 1):
        choice_name = 'Rock'
    elif(choice == 2):
        choice_name = 'Paper'
    else:
        choice_name = 'Scissors'
    
    # print user choice 
    print("User choice is: ", choice_name)
    print("Now it's Computer's Turn...")

    # computer chooses randomly any number among 1, 2 and 3
    comp_choice = random.randint(1, 3)

    # initialize value of comp_choice_name variable corresponding to the choice value 
    if(comp_choice == 1):
        comp_choice_name = 'Rock'
    elif(comp_choice == 2):
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissors'

    print("Computer choice is: ", comp_choice_name)
    print(choice_name + " VS " + comp_choice_name)

    # determine the winner
    if(choice == comp_choice):
        result = 'DRAW'
    elif((choice == 1 and comp_choice == 2) or (choice == 2 and comp_choice == 1)):
        result = 'Paper'
    elif((choice == 1 and comp_choice == 3) or (choice == 3 and comp_choice == 1)):
        result = "Rock"
    elif((choice == 2 and comp_choice == 3) or (choice == 3 and comp_choice == 2)):
        result = 'Scissors'
    
    # print the result 
    if(result == 'DRAW'):
        print("<== It's a tie! ==>")
    elif(result == choice_name):
        print('<== User wins! ==>')
    else:
        print('<== Computer Wins! ==>')
    
    print('Do you want to play angain ? (Y / N)')
    ans = input().lower()
    if(ans == 'n'):
        break

print('Thanks for playing!\n')