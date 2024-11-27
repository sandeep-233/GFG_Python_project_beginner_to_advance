import random

# the .randrange() function genereate a random number within the specified range 
num = random.randrange(1000, 10000)

n = int(input("Guess the 4 digit number: "))

# condition to test equality of the guess made. Program terminates if true 
if(n == num):
    print("Great! You guessed the number in just 1 try! You're a Mistermind!")
else :
    # ctr variable initialized. It will keep count of the number of tries the Player takes to guess the number 
    ctr = 0

    # while loop repeats as long as the Player fails to guess the number correctly 
    while(n != num):
        # varibel increment every time the loop is executed, given an idea of how many guesses were made.
        ctr += 1

        cnt = 0

        # explicit type conversion of an interger to a string in order to ease extraction of digits 
        n_str = str(n)
        num_str = str(num)

        # correct[] list stores digits which are correct 
        correct = ['X']*4

        # for loop runs 4 times since the number has 4 digits
        for i in range(0, 4):
            # checking for equality of digits
            if(n_str[i] == num_str[i]):
                # number of digits gueesed correctly increments
                cnt += 1
                # hence, the digit is stored in correct[] 
                correct[i] = n_str[i]
            else:
                continue

        # when not all the digits are guessed correctly.
        # if (cnt < 4) and (cnt != 0):- this condition is not needed as we are starting with the condition, n != num, which is, cnt < 4
        print("Not quite the number. But you did get ", cnt, " digit(s) correct!")

        # print("Also these numbers in your input were correct.")
        for k in correct:
            print(k, end=' ')

        print('\n')
        print('\n')

        n = int(input("Enter your next choise of numbers: "))

    if(n == num):
        print("You've become a Mastermind! \nIt took you only ", ctr+1, " tries.")
        