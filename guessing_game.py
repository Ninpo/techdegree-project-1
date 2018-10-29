"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
"""

import random


def display_banner():
    banner = """--------------------------------------
                |Welcome to the Number Guessing Game!|
                --------------------------------------
                |  Press CTRL+C to quit at any time. |
                --------------------------------------"""
    return "\n".join(banner_line.lstrip() for banner_line in banner.splitlines())


def get_player_guess():
    try:
        player_guess = int(input("Pick a number between 1 and 10: "))
        if player_guess > 10 or player_guess < 1:
            raise ValueError
        return player_guess
    except ValueError:
        print("Input error, please enter an integer from 1 to 10")
        return get_player_guess()


def check_guess(correct_number, player_guess):
    if player_guess > correct_number:
        print("It is lower!")
        return False

    if player_guess < correct_number:
        print("It is higher!")
        return False

    return correct_number == player_guess


def play_again_prompt():
    play_again = input("Would you like to play again? [y]es/[n]o: ")
    if play_again.lower().startswith("y"):
        return True
    elif play_again.lower().startswith("n"):
        return False
    else:
        print("I did not understand.")
        return play_again_prompt()


def end_game(high_score):
    print("\nThe best score you achieved was {}.".format(high_score))
    print("Closing the game, see you next time!")


def start_game():
    print(display_banner())
    attempts = 0
    high_score = 0
    correct_number = random.randint(1, 10)
    try:
        while True:
            player_guess = get_player_guess()
            attempts += 1
            if not check_guess(correct_number, player_guess):
                continue
            print("You got it! It took you {} tries".format(attempts))
            if not high_score or attempts < high_score:
                high_score = attempts
            if not play_again_prompt():
                end_game(high_score)
                break
            print("The HIGHSCORE is {}".format(high_score))
            attempts = 0
    except KeyboardInterrupt:
        end_game(high_score)


if __name__ == "__main__":
    # Kick off the program by calling the start_game function.
    start_game()
