import random


secret_number = str((random.randint(1000, 9999)))

while True:
    print(secret_number)
    guess = input("what is your guess? 4 digit number! ")
    cows = 0
    bulls = 0
    print(guess)
    if guess != secret_number:
        for i in range(4):
            if secret_number[i] == guess[i]:
                bulls += 1
            elif guess[i] in secret_number:
                cows += 1

        print("cows:", cows, "bulls:", bulls)
    else:
        print("you guess right the number was: ", secret_number)
        break
sample: list[int] = [1, 2, 3, "1"]
