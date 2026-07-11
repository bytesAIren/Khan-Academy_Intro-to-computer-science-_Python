import typer

print("Type the words and hit enter within the time limit!")

# Play three rounds of a speed typing game.
for level in range(1, 6):
    print("--- LEVEL " + str(level) + " ---")

    how_many_words = typer.get_level_words_count(level)
    which_mode = typer.get_level_mode(level)
    time_limit = typer.get_level_time_limit(level)
    
    words_to_type = typer.pick_random_words(how_many_words, which_mode)
    passed = typer.play_round(words_to_type, time_limit)
    if not passed:
        print("Oops!")
        break 
    highest_level = level

# Fine del gioco: resoconto dei progressi
print("\n--- GAME OVER ---")
if highest_level == 5:
    print("Amazing! You completed all 5 levels!")
else:
    print("You reached Level " + str(highest_level) + ". Try again to beat your record!")

print("Thanks for playing.")

