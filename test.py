import math
import random

lower_bound = int(input("what is the lowerbound? "))
upper_bound = int(input("what is the upperbound? "))
minimum_guess = int(math.log(upper_bound - lower_bound + 1))
rand = random.randint(lower_bound, upper_bound)
while True:

    guess_rand = int(input("what is your guess "))
    if guess_rand < rand and minimum_guess != 0:
        print("Try Again! You guessed too small")
        minimum_guess -= 1
        print(minimum_guess)
    elif guess_rand > rand and minimum_guess != 0:
        print("Try Again! You guessed too high")
        minimum_guess -= 1
        print(minimum_guess)
    elif guess_rand == rand and minimum_guess != 0:
        print("congratulations!")
        break
    elif minimum_guess == 0:
        print("better luck next time")
        print(rand)
        break
