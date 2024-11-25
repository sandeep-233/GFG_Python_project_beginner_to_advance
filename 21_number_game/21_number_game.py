# return the nearest mulitple to 4
def nearestMultiple(num):
    if(num >= 4):
        near = num + (4 - (num % 4))
    else:
        near = 4
    return near

def lose1():
    print("\n\n You Lose!")
    print("Better luch next time!")
    exit(0)

# check wheter the number are consecutive
def check(xyz):
    i = 1
    while(i<len(xyz)):
        if (xyz[i]-xyz[i-1]) != 1:
            return False
        i = i+1
    return True

# start game
def start1() :
    xyz = []
    last = 0

    while True:
        print("Enter 'F' to take the first chance.")
        print("Enter 'S' to take the second chance.")
        chance = input('> ')

        # player takes the first chance 
        if chance == 'F':
            while True:
                if last == 20:
                    lose1()
                else:
                    print ("\n Your Turn.")
                    print("\nHow many numbers do you wish to enter?")
                    inp = int(input('> '))

                    if inp > 0 and inp <= 3:
                        comp = 4-inp
                    else:
                        print("Wrong input. You are disqualified from the game.")
                        lose1()

                    i, j = 1, 1

                    print("Now enter the values")
                    while i <= inp:
                        a = input('> ')
                        a = int(a)
                        xyz.append(a)
                        i = i+1
                    
                    # store the last element of xyz
                    last = xyz[-1]

                    # checks whether the input 
                    # number are consecutive
                    if(check(xyz) == True):
                        if(last == 21):
                            lose1()
                        else:
                            # computer's turn
                            while j <= comp:
                                xyz.append(last+j)
                                j = j+1
                            print("Order if inputs after computer's turn is: ")
                            print(xyz)
                            last = xyz[-1]
                    else:
                        print("\nYou did not input consecutive integers.")
                        lose1()

        # player takes the second chance 
        elif chance == 'S':
            comp = 1
            last = 0

            while last<20:
                xyz.append(last+j)
                j = j+1
            
            print("Order of inputs after computer's turn is: ")
            print(xyz)
            if xyz[-1] == 20:
                lose1()
            else:
                print("\nYour Turn.")
                print("\nHow many numbers do you wish to enter?")
                inp = input('> ')
                inp = int(inp)
                i = 1
                print("Enter your values")
                while i <= inp:
                    xyz.append(int(input('> ')))
                    i = i+1
                last = xyz[-1]
                if check(xyz) == True:
                    # print xyz
                    near = nearestMultiple(last)
                    comp = near - last
                    if comp == 4:
                        comp = 3
                    else:
                        comp = comp
                else:
                    # if inputs are not consecutive
                    # automaticaly disqualified
                    print("\nYou did not input consecutive integers.")
                    lose1()
            print("\n\nCONGRATULATION !!!")
            print("YOU WON!")
            exit(0)
        else:
            print("Worng Choice")

game = True
while game == True:
    print("Player 2 is Computer.")
    print("Do you want to play the 21 Number Game? (Yes / No)")
    ans = input('> ')
    
    if(ans == 'Yes'):
        start1()
    else:
        print("Do you want quit the game? (Yes / No)")
        nex = input("> ")
        if(nex == 'Yes'):
            print("You are quitting the game...")
            exit(0)
        elif(nex == 'No'):
            print('Continuing...')
        else:
            print("Wrong choice")