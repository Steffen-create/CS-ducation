# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(" ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()

def has_player_won(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for char in secret_word:
        if char not in letters_guessed:
            return False
    return True


def get_word_progress(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    message = ""
    for char in secret_word:
        if char in letters_guessed:
          message += char
        else:
          message += "*"
    return message



def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    alphabet = string.ascii_lowercase
    letters_left = ""
    for char in alphabet:
        if char not in letters_guessed:
            letters_left += char
    return letters_left


def hangman(secret_word, with_help):
    """
    secret_word: string, the secret word to guess.
    with_help: boolean, this enables help functionality if true.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a single letter (or help character '!'
      for with_help functionality)

    * If the user inputs an incorrect consonant, then the user loses ONE guess,
      while if the user inputs an incorrect vowel (a, e, i, o, u),
      then the user loses TWO guesses.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    -----------------------------------
    with_help functionality
    -----------------------------------
    * If the guess is the symbol !, you should reveal to the user one of the
      letters missing from the word at the cost of 3 guesses. If the user does
      not have 3 guesses remaining, print a warning message. Otherwise, add
      this letter to their guessed word and continue playing normally.

    Follows the other limitations detailed in the problem write-up.
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    #initialization
    remaining_guesses = 10
    remaining_letters = string.ascii_lowercase
    picked_letters = ""
    output_word = get_word_progress(secret_word, picked_letters)
    victory = False
    vowels = "aeiou"

    valid_input = string.ascii_letters
    if with_help:
        valid_input += "!"
    print("Welcome to Hangman!", f"I am thinking of a word that is {len(secret_word)} letters long.", sep= "\n")
    
    #MNain game loop
    while remaining_guesses > 0:
        print("-------------",
              f"You have {remaining_guesses} guesses left.",
              f"Available letters: {remaining_letters}",
              sep= "\n")
        user_input = input("Please guess a letter: ")
        
        #help functionality
        if user_input == "!" and with_help:
           if remaining_guesses > 3:
              remaining_guesses -= 3
              revealed_letter = secret_word[output_word.index("*")]
              picked_letters += revealed_letter
              remaining_letters = remaining_letters.replace(revealed_letter, "")
              output_word = get_word_progress(secret_word, picked_letters)
              print(f"Letter revealed: {revealed_letter}", output_word, sep= "\n")
              if has_player_won(secret_word, picked_letters):
                victory = True
                break
           else:
              print(f"Oops! Not enough guesses left: {output_word}")
        elif user_input not in valid_input:
          print(f"Oops! That is not a valid letter. Please input a letter from the alphabet: {output_word}")
        elif str.lower(user_input) not in remaining_letters:
          print(f"Oops! You've already guessed that letter: {output_word}")
        else: #legal input that must be handled
          user_input = str.lower(user_input)
          picked_letters += user_input
          remaining_letters = remaining_letters.replace(user_input, "")
          if output_word == get_word_progress(secret_word, picked_letters):
            if user_input in vowels:
              remaining_guesses -= 2
            else:
              remaining_guesses -= 1
            print(f"Oops! That letter is not in my word: {output_word}")
          else:
            output_word = get_word_progress(secret_word, picked_letters)
            print(f"Good guess: {output_word}")
            if has_player_won(secret_word, picked_letters):
              victory = True
              break


    #end of game
    print("-------------")
    if victory:
      total_score = remaining_guesses + 4 * len(set(secret_word)) + 3*len(secret_word)
      print("Congratulations, you won!",
            f"Your total score for this game is: {total_score}",
            sep= "\n")
    else:
      print(f"Sorry, you ran out of guesses. The word was {secret_word}.")
        



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test

if __name__ == "__main__":
    # To test your game, uncomment the following three lines.

    secret_word = choose_word(wordlist)
    secret_word = "hi"
    with_help = True
    hangman(secret_word, with_help)

    # After you complete with_help functionality, change with_help to True
    # and try entering "!" as a guess!

    ###############

    # SUBMISSION INSTRUCTIONS
    # -----------------------
    # It doesn't matter if the lines above are commented in or not
    # when you submit your pset. However, please run ps2_student_tester.py
    # one more time before submitting to make sure all the tests pass.
  

