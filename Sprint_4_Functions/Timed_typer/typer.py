"""Plays a game where the user types random words within a time limit."""

import random
import time
import word_bank

def play_round(words, seconds):
    """Returns True if the user successfully completed the round."""
    # Run a stopwatch for the time it takes the user to respond.
    start = time.time()
    response = input("(" + str(seconds) + " seconds) " + words + "\n")
    stop = time.time()

    # Fail the round if a word is mispelled or if time runs out.
    within_time_limit = stop - start < seconds
    return response == words and within_time_limit

def pick_random_words(num_words, word_length):
    """Returns a random phrase containing the given number of words.""" 
    words = ""
    for word in range(num_words):
        word = get_random_word(word_length)
        words = words + " " + word

    return words.strip()

def get_random_word(mode):
    """Returns a random word with a word length based on the given mode."""
    if mode == "hard":
        words = word_bank.hard_words
    elif mode == "medium":
        words = word_bank.medium_words
    else:
        words = word_bank.easy_words

    return random.choice(words)

def get_level_words_count(level):
    """Decides how many words the user has to type in a single round."""
    if level == 1 or level == 2:
        return 1
    elif level == 3 or level >= 4:
        return 2
    else:
        return 3

def get_level_mode(level):
    """decides how many words the user must type for each level"""
    if level == 1:
        return "easy"
    elif level == 2 or level == 3:
        return "medium"
    elif level >= 4:
        return "hard"

def get_level_time_limit(level):
    """decides how many seconds the user has to write the words"""
    if level == 1 or level == 3:
        return 10
    elif level == 2:
        return 7
    elif level == 4:
        return 8
    else:
        return 6
    



        
