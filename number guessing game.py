import random


def game():
    play = True 
    while(play):
        #Below, we introduct the opeining question which makes the game more personal.
        print("Hey, What is your name?")
        player = input() #here were take the input pf the player.

        print("Well", player, "Let's have some fun in this nuber guessing game. I am thinking of a number between 1 and 20.")
        print("to quit game enter 0")

        range=input("Would you want to choose your range? Answer in yes or no")#here we are giving a choice to the player to choose the range
        if range==("yes"):
            min=int(input("lower range"))
            max=int(input("higher range"))
            N = random.randint(min,max)   # N has to defined
        if range == ("no"):
            N = random.randint(1,100)

        #N=random.randint(1,20)#main function to call to start the guessing game, in this the computer lets the player guess the number.
        #N=7 #we define what N is, the number to be guessed

        tries = 0
        guess = 1
        guess = int(input("Enter your guess as a positive integer:"))
        print("to quit game enter 0")

        #true = N #we define that true is the player guessing the right number

        #while true: #gives the function if player guessed the right number.
        while (tries <=5):   #code modified  by prof ferguson
            #guess = int(input("Enter your guess as a positive integer:"))
            #print("to quit game enter 0")  # moved to bottom of loop

            tries += 1
            if tries >= 5: #limits number of tries
                print ("Sorry. You tried too many times.")
                print ("The number was", N)
                #restart = str(input("Do you want to play again? Enter yes or no"))
                #if restart == "no":
                    #print("Goodbye")
                play = False
                break

            if (guess > N):
                print("Sorry, your guess is too high")
            elif guess < N:
                print("Sorry, your guess is too low.")

            guess = int(input("Enter your guess as a positive integer:"))
            print("to quit game enter 0")

            #if guess ==N:
        print("HEY! Congratulation, you guessed the rght number -" ,N)
        print("It took you", tries, "tries.)\n")

        tries = 1
        restart = str(input("Do you want to play again? Enter yes or no"))
        if restart == "no":
            print("Goodbye")
            play = False
            break
        if restart == "yes":
            game()

game()
input("\n\nPress the enter key to exit.")
