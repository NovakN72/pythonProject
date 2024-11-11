import random

words = [
    "rainbow",
    "computer",
    "science",
    "programming",
    "python",
    "mathematics",
    "player",
    "condition",
    "reverse",
    "water",
    "board",
    "geeks",
]
word = random.choice(words)
guesses = input("guess the letters ")
turns = 12

while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            if turns < 12:
                print("NOPE!!!")
            print("_")
            failed += 1
            turns -= 1

    if failed == 0:
        print("congrats the word is", word)
        break
    guess = input("guess a character")
    guesses += guess
    # if guess not in word:
    #    print("wrong")
