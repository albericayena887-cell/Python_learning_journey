numbers = 4
guess = 0
while guess != numbers:
    guess = int(input("Le nombre doit etre entre(1-4): "))
    if guess != numbers:
        print("Mauvaise reponse")

print("Bonne réponse")    