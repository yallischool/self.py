import random
import os

def choose_word(file_path, word_file_name):
    """
    Chooses a random word from a file.

    Args:
    - file_path (str): The path to the file containing words.

    Returns:
    - str: The chosen word.
    """
    while True:
        if os.path.exists(word_file_name):
            break
        else:
            print("File is not found, try again")
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
    - str: A string with underscores representing unguessed letters and correctly guessed letters.
    """
    display_word = ""
    for char in secret_word:
        if char in old_letters_guessed:
            display_word += char
        else:
            display_word += "_"
    return display_word

# Example usage:
secret_word = choose_word("words.txt", "word_list.txt")
guessed_letters = []
print(show_hidden_word(secret_word, guessed_letters))
