# Display the title and other functions before the game starts

import time
import dbinteract

def get_player_name():
    title = """
*********************************************************************  
 __  _  _ ____ ____ _ ____ ____ _  _    ___ _   _ ____ ____ ____ _  _ 
|__| |\/| |___ |__/ | |    |__| |\ |     |   \_/  |    |  | |  | |\ | 
|  | |  | |___ |  \ | |___ |  | | \|     |    |   |___ |__| |__| | \|

*********************************************************************

                        1. New Game
                        2. Continue
                        3. Quit
"""
    print(title)

    user_input = input("Enter your choice: ")   

    while user_input not in ["1", "2", "3"]:
        print("Invalid input. Please try again.")
        user_input = input("Enter your choice: ")

    if user_input == "1":
        player_name = input("Please enter your name: ")
        while player_name.title() in dbinteract.get_existing_names():
            player_name = input("Name already exists. Please enter a new name: ")
        dbinteract.register_new_player(player_name.title())

        print(f"Welcome to American Tycoon! {player_name.title()}!")

        return player_name.title()

    elif user_input == "2":
        if not dbinteract.get_existing_names():
            print("\nNo unfinished game found. Please start a new game.")
            time.sleep(3) # Pause for 3 seconds before display the title again.
            get_player_name()
        else:
            player_name = get_saved_name()
            print(f"Welcome back! {player_name.title()}!")

            return player_name.title()

    elif user_input == "3":
        exit()

def get_saved_name():
    print("-----------------------------")
    print("Unfinished games: ")
    for index, name in enumerate(dbinteract.get_existing_names()):
        print(f"{index + 1}. {name}")
    print("-----------------------------")
    player_name = input("Please enter your name: ")
    while player_name.title() not in dbinteract.get_existing_names():
        player_name = input("Invalid names. Please try again: ")

    return player_name

def read_intro():
    prompt = f"Do you want to read the introduction?(y/n)"
    user_input = input(prompt)
    while user_input.lower() not in ["y", "n"]:
        print("Invalid input. Please try again.")
        user_input = input(prompt)

    if user_input.lower() == "n":
        return None
    else:
        introduction = """
        ------------------------------------------------------------------------------------------------------------------------
        You are an ambitious green hand who is ready to become the richest tycoon in the U.S.
        The first step of your commercial legend is to make more than 1,000,000 dollars during the next 15 days(360 hours).
        In the beginning of your journey, you will start at a random place with 10,000 dollars as your initial capital.
        After that, you can freely buy or sell goods from local stores before the time limit.
        You can also choose to move up to 15 different places in the U.S.
        Be aware that traveling takes time which depends on the distance between your current location and the destination.
        Good luck!
        ------------------------------------------------------------------------------------------------------------------------
        """
        print(introduction)
