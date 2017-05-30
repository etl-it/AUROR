import os


def menu():
    #Clean the screen and show the menu once more
    os.system('clear')
    print('Select an option:')
    print("\t1 - DEFAULT")
    print("\t2 - PERSONALIZE TEST")
    print("\t3 - Goodbye AUROR")


while True:
    #Show the menu
    menu()

    #Ask for an option to the user
    optionMenu = input("Insert an option: >> ")

    if optionMenu == 1:
            print("Auror will operate in default mode. You dont have to configure any other parameter")
    elif optionMenu2 == 2:
        print("You are gonna to personalize your own test")
        optionMenu2 = input("Please, select the configure parameters >>")
