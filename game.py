# The main game function

import title

GAME_TARGET = 1_000_000
TIME_LIMIT = 15 # days

player_name = title.get_player_name()

# Get current_day of the player from the database, if current_day > TIME_LIMIT => Game Over! => Back to title?

# Get current_funds of the player from the database, if current_funds > GAME_TARGET => Congratulations! => Thank you for playing?

# Ask the players if they want to read the introduction or not
    # Write a display_introduction function

# Get the information of the player from database and display it.

# Ask the player for command
 # 1. Check goods list of local store
    # - 1. Display the goods list of the local store
    # - 2. Buy something => Update the inventory
    # - 3. Sell something => update the inventory
    # - 4. Back
 # 2. Move to another airport
    # - 1. List the airports table
            # -- 1. Input the airport_ident
            # -- 2. Display the distance and time the travel costs
              # --- 1. Yes => Move to new airport
              # --- 2. No => Back
    # - 2. Back
 # 3. Check inventory
    # - 1. List the inventory table
    # - 2. Back
 # 4. Quit the game
