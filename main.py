import random
import os

def choose_word(file_path, index):
    with open(file_path, "r") as file:
        words = file.read().split()
        chosen_word = words[(index - 1) % len(words)]
        return chosen_word.lower()

def check_valid_input(letter_guessed, old_letters_guessed):
    if len(letter_guessed) != 1 or not letter_guessed.isalpha():
        return False
    if letter_guessed in old_letters_guessed:
        return False
    return True

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if not check_valid_input(letter_guessed, old_letters_guessed):
        print(" -> ".join(sorted(old_letters_guessed)))
        return False
    old_letters_guessed.append(letter_guessed)
    return True

def show_hidden_word(secret_word, old_letters_guessed):
    revealed_word = ""
    for letter in secret_word:
        if letter in old_letters_guessed:
            revealed_word += letter + " "
        else:
            revealed_word += "_ "
    return revealed_word.strip()

def check_win(secret_word, old_letters_guessed):
    for letter in secret_word:
        if letter not in old_letters_guessed:
            return False
    return True

def main():
    MAX_TRIES = 6
    file_path = input("enter input file name: ")
    index = int(input("enter a number"))
    secret_word = choose_word(file_path, index)
    old_letters_guessed = []

    print("Let's play Hangman!")
    print("""
    Welcome to the game Hangman
    _    _                                         
    | |  | |                                        
    | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
    |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
    | |  | | (_| | | | | (_| | | | | | | (_| | | | |
    |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |                      
                        |___/
    """)
    print("The word contains", len(secret_word), "letters.")
    while MAX_TRIES > 0:
        print("------------")
        print("Attempts left:", MAX_TRIES)
        letter_guessed = input("Guess a letter: ").lower()
        if try_update_letter_guessed(letter_guessed, old_letters_guessed):
            if letter_guessed in secret_word:
                revealed_word = show_hidden_word(secret_word, old_letters_guessed)
                print(revealed_word)
                if check_win(secret_word, old_letters_guessed):
                    print("""
                    
                    
                    
                    
                    ___.__. ____  __ __  __  _  ______   ____  
                    <   |  |/  _ \|  |  \ \ \/ \/ /  _ \ /    \ 
                    \___  (  <_> )  |  /  \     (  <_> )   |  \\
                    / ____|\____/|____/    \/\_/ \____/|___|  /
                    \/                                      \/ 
                            
                    
                    """)    
                    return
            else:
                MAX_TRIES -= 1
                print("Wrong guess!")
                print_hangman(MAX_TRIES)
        else:
            print("Invalid input. Please enter a single letter that has not been guessed before.")

    print("""                                                         
   _________    _____   ____     _______  __ ___________ 
  / ___\__  \  /     \_/ __ \   /  _ \  \/ // __ \_  __ \\
 / /_/  > __ \|  Y Y  \  ___/  (  <_> )   /\  ___/|  | \/
 \___  (____  /__|_|  /\___  >  \____/ \_/  \___  >__|   
/_____/     \/      \/     \/                   \/       """)
    print("The word was:", secret_word)

def print_hangman(num_tries):
    hangman_pics = [
        """
        x-------x
        |       |
        |       0
        |      /|\\
        |      / \\
        |

        """,
        """
        x-------x
        |       |
        |       0
        |      /|\\
        |      /
        |   
        """,
        """
        x-------x
        |       |
        |       0
        |      /|\\
        |
        |
        """,
        """
        x-------x
        |       |
        |       0
        |       |
        |
        |
        """,
        """
        x-------x
        |       |
        |       0
        |
        |
        |
        """,
        """
        x-------x
        |
        |
        |
        |
        |
        """,
        """
        x-------x  
        """
    ]
    print(hangman_pics[num_tries])
if __name__ == "__main__":
    main()
