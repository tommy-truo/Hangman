from os import name, system
import random
import collections


def clear_console():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


def choose_word():
    choose_custom = input("Do you want a randomly chosen word, or would you like to choose a custom word for you or someone else to guess?\n\n[1. Randomly Chosen, 2. Custom Word]\n>>>> ")

    while choose_custom.lower() not in ['1', 'randomly chosen', '2', 'custom word']:
        print("\n\nThat is not an option.\n\n")

        choose_custom = input("Do you want a randomly chosen word, or would you like to choose a custom word for you or someone else to guess?\n\n[1. Randomly Chosen, 2. Custom Word]\n>>>> ")

    if choose_custom.lower() in ['1', 'randomly chosen']:
        word_choices = ('keyboard', 'mouse', 'supercalifragilisticexpialidocious', 'hangman', 'power', 'fans', 'python', 'behemoth', 'windows', 'monitor', 'computer', 'play', 'understandable', 'perhaps', 'passive', 'relief', 'spite', 'relaxation', 'vacation', 'stress', 'uncertainty', 'unknown', 'unbeknown', 'devotion', 'worship', 'elegance', 'waste', 'inadequate', 'inferior', 'hopeless', 'useless', 'perfection', 'satisfactory', 'capable', 'possible', 'curvature', 'sustainable', 'cheesy', 'detestable', 'grace', 'witness', 'gatekeeper', 'despair', 'hope', 'ambition', 'productive', 'brackets', 'parentheses', 'exactly', 'taciturn', 'obnoxious', 'sympathetic', 'sessions', 'prideful', 'proud', 'sects', 'firmly', 'two-faced', 'no-face', 'deteriorate', 'terrace', 'house', 'government', 'overthrow', 'capitalists', 'communism', 'socialists', 'programs', 'clarity', 'closure', 'average', 'typical', 'decent', 'fined', 'opposite', 'similar', 'consciousness', 'introduction', 'progression', 'regression', 'translation', 'language', 'tie', 'draw', 'landslide', 'midnight', 'twilight', 'limelight', 'dusk', 'disco', 'beauty', 'companion', 'played', 'unfaithful', 'enjoy', 'mind', 'dance', 'hatred', 'fortunate', 'sturdy', 'stable', 'mine', 'craft', 'terrain', 'instant', 'flash', 'twenty', 'five', 'advanced', 'lists', 'sunglasses', 'ribbons', 'bows', 'scarfs', 'boards', 'bored', 'homonym', 'plural', 'platform', 'ligaments', 'tendon', 'tenderloin', 'ribeye', 'embarrass', 'embarrassment', 'headache', 'escape', 'beg', 'peace', 'wires', 'cables', 'buttons', 'pen', 'utensil')

        hidden_word = random.choice(word_choices)

    elif choose_custom.lower() in ['2', 'custom word']:
        hidden_word = input("\n\nWhat do you want the guessed word to be?\n\n>>>> ")

    clear_console()
    
    return hidden_word


def guess_char(word, corr_list, incorr_list):
    new_guess = input("\nGuess a new letter\n>>>> ")

    while len(new_guess) > 1 or new_guess.isalpha() == False:
        if len(new_guess) > 1:
            print("\nDon't cheat! Guess only one letter at a time!")

            new_guess = input("\nGuess a new letter\n>>>> ")

        elif new_guess.isalpha() == False:
            print("\nPlease only guess with letters in the alphabet.")

            new_guess = input("\nGuess a new letter\n>>>> ")

    if new_guess in word:
        corr_list.append(new_guess)

    else:
        incorr_list.append(new_guess)


def game_screen(word, corr_list, incorr_list):
    hangman_pics = {
        0 : """\n+---+
|
|
|
=====""",
        1 : """\n+---+
|   o
|
|
=====""",
        2 : """\n+---+
|   o
|   |
|
=====""",
        3 : """\n+---+
|   o
|  /|
|
=====""",
        4 : """\n+---+
|   o
|  /|\\
|
=====""",
        5 : """\n+---+
|   o
|  /|\\
|  /
=====""",
        6 : """\n+---+
|   o
|  /|\\
|  / \\
====="""
    }
    
    word_len = []
        
    for char in word:
        if char == '-':
            word_len.append("- ")

        elif char in corr_list:
            word_len.append(char + " ")

        else:
            word_len.append("_ ")
    word_len = "".join(word_len)

    if len(incorr_list) > 0:
        incorr_chars = "\nIncorrect letters: "

        for char in incorr_list:
            incorr_chars = incorr_chars + char + ", "
        
        return word_len, hangman_pics[len(incorr_list)], incorr_chars
    
    else:
        return word_len, hangman_pics[len(incorr_list)]


def retry(func):
    retry = input("\nWould you like to play again?\n\n[y/n]\n>>>> ")

    while retry.lower() not in ['y', 'n']:
        print("\n\nThat is not an option\n")

        retry = input("\nWould you like to play again?\n\n[y/n]\n>>>> ")

    if retry.lower() == 'y':
        func()

    elif retry.lower() == 'n':
        print("\n\nUnderstandable, have a great day.")


def game():
    clear_console()
    
    hidden_word = choose_word()

    corr_char = []

    incorr_char = []

    while True:
        clear_console()
        
        if len(incorr_char) > 0:
            word_len, hangman_pic, incorr_chars = game_screen(hidden_word, corr_char, incorr_char)

            print(hangman_pic)
            
            print("\n\n" + word_len)

            print(incorr_chars)

        else:
            word_len, hangman_pic = game_screen(hidden_word, corr_char, incorr_char)

            print(hangman_pic)
            
            print("\n\n" + word_len)

        guess_char(hidden_word, corr_char, incorr_char)

        if len(incorr_char) > 0:
            word_len, hangman_pic, incorr_chars = game_screen(hidden_word, corr_char, incorr_char)

        else:
            word_len, hangman_pic = game_screen(hidden_word, corr_char, incorr_char)

        if len(incorr_char) == 6:
            clear_console()
            
            print(hangman_pic)

            print("\n\n" + word_len)
            
            print("\nYou lost! The chosen word was " + hidden_word + "!")
            
            break

        if "_ " not in word_len:
            clear_console()
            
            print(hangman_pic)

            print("\n\n" + word_len)
            
            print("\nYou won! You successfully guessed " + hidden_word + "!")

            break

    retry(game)


def start_game():
    clear_console()
    
    game_start = input("Do you want to play Hangman?\n\n[y/n]\n>>>> ")

    while game_start.lower() not in ['y', 'n']:
        print("\n\nThat is not an option.\n\n")

        game_start = input("Do you want to play Hangman?\n\n[y/n]\n>>>> ")

    if game_start.lower() == 'n':
        print("\n\nUnderstandable, have a great day.")

    elif game_start.lower() == 'y':
        game()


def main():
    start_game()


if __name__ == "__main__":
    main()