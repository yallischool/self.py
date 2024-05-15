import random
import os

#choose word
def choose_word(file_path):
    print("input your file name \nif you want the defult use words.txt")
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
#choose word end

#input is valid
def check_valid_input(letter_guessed, old_letters_guessed):
    if len(letter_guessed) != 1 or not letter_guessed.isalpha():
        return False
    if letter_guessed in old_letters_guessed:
        return False
    return True
#input is valid end

#update letter
def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if not check_valid_input(letter_guessed, old_letters_guessed):
        print(" -> ".join(sorted(old_letters_guessed)))
        return False
    old_letters_guessed.append(letter_guessed)
    return True
#update letter end

#show word 
def show_hidden_word(secret_word, old_letters_guessed):
    revealed_word = ""
    for letter in secret_word:
        if letter in old_letters_guessed:
            revealed_word += letter + " "
        else:
            revealed_word += "_ "
    return revealed_word.strip()
#show word end

#check win
def check_win(secret_word, old_letters_guessed):
    for letter in secret_word:
        if letter not in old_letters_guessed:
            return False
    return True
#check win end

#main func " hangman " end
def hangman():
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

    print("Game over")
    print("The word was:", secret_word)
#main func " hangman " end 


#print pics
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
#print pics end

hangman()
