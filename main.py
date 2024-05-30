import random
import os

def choose_word(file_path):
    """
    Chooses a random word from a file.

    Args:
    - file_path (str): The path to the file containing words.

    Returns:
    - str: The chosen word.
    """
    while True:
        word_file_name = input("file name: ")
        if os.path.exists(word_file_name):
            break
        else:
            print("file is not found, try again")
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, word_file_name)
    with open(file_path, "r") as file:
        words = file.read().split()
        chosen_word = random.choice(words)
        return chosen_word.lower()

def check_valid_input(letter_guessed, old_letters_guessed):
    """
    Checks if the guessed letter is valid.

    Args:
    - letter_guessed (str): The letter guessed by the user.
    - old_letters_guessed (list): List of letters previously guessed.

    Returns:
    - bool: True if the input is valid, False otherwise.
    """
    if len(letter_guessed) != 1 or not letter_guessed.isalpha():
        return False
    if letter_guessed in old_letters_guessed:
        return False
    return True

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    Tries to update the guessed letters list.

    Args:
    - letter_guessed (str): The letter guessed by the user.
    - old_letters_guessed (list): List of letters previously guessed.

    Returns:
    - bool: True if the letter was successfully added, False otherwise.
    """
    if not check_valid_input(letter_guessed, old_letters_guessed):
        print(" -> ".join(sorted(old_letters_guessed)))
        return False
    old_letters_guessed.append(letter_guessed)
    return True

def show_hidden_word(secret_word, old_letters_guessed):
    """
    Generates a string showing the hidden letters of the word.

    Args:
    - secret_word (str): The word to be guessed.
    - old_letters_guessed (list): List of letters previously guessed.

    Returns:
    - str: A string showing the hidden letters of the word.
    """
    revealed_word = ""
    for letter in secret_word:
        if letter in old_letters_guessed:
            revealed_word += letter + " "
        else:
            revealed_word += "_ "
    return revealed_word.strip()

def check_win(secret_word, old_letters_guessed):
    """
    Checks if the player has guessed all the letters in the word.

    Args:
    - secret_word (str): The word to be guessed.
    - old_letters_guessed (list): List of letters previously guessed.

    Returns:
    - bool: True if all letters have been guessed, False otherwise.
    """
    for letter in secret_word:
        if letter not in old_letters_guessed:
            return False
    return True

def main():
    """
    Main function to run the Hangman game.
    """
    MAX_TRIES = 6
    file_path = "word.txt" 
    secret_word = choose_word(file_path)
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
    """
    Prints the Hangman ASCII art corresponding to the number of tries left.

    Args:
    - num_tries (int): Number of attempts left.
    """
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
