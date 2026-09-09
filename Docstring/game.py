import random
while True:
    try:
        n = int(input("Level: "))

        if n > 0:
            break
    except ValueError:
        continue


user = random.randint(1, n)
while True:
    try:
        guess = int(input("Guess: "))
        if guess < user:
            print("Too small!")
        elif guess > user:
            print("Too large!")
        else:
            print("Too right!")
            break
    except ValueError:
        continue

