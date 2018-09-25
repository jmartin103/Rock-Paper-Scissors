import random

def menu():
    print("Select an option from the menu: ")
    print("1 - Rock\n2 - Paper\n3 - Scissors")

while True:
    menu()

    randNum = random.randint(1, 3)
    userInput = int(input("Please select your choice: "))

    if userInput == randNum:
        print("It's a draw! Let's go again!")
    elif userInput == 1: # User selects rock
        if random == 2: # Computer selects paper
            print("Sorry, you lose!")
        else: # Computer selects scissors
            print("Congrats! You win!")
    elif userInput == 2: # User selects paper
        if random == 1: # Computer selects rock
            print("Congrats! You win!")
        else: # Computer selects scissors
            print("Sorry, you lose!")
    elif userInput == 3: # User selects scissors
        if random == 1: # Computer selects rock
            print("Sorry, you lose!")
        else: # Computer selects paper
            print("Congrats! You win!")
    else:
        print("Invalid option; please try again.")
        continue

    choice = raw_input("Would you like to play again (Y/N)? ")
    if choice == 'y' or choice == 'Y':
        continue
    elif choice == 'n' or choice == 'N':
        print("Thanks for playing! See you again next time!")
        break
