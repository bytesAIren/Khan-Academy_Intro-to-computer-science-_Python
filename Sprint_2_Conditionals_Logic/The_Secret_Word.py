secret_word = "mellow"

user_word = input ("Guess the secret word:" " ") 
norm_user_word = user_word.lower()

if "please" in norm_user_word and "hint" in norm_user_word:
    print ("Something sweet and comfy")
elif "please" in norm_user_word:
    print ("Your flattery is in vain. Access denied!")
elif norm_user_word == secret_word:
    print ("Correct!")
else:
    print ("Wrong!")
