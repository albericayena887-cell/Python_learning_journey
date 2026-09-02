nom = input("Ecris un mot: ").lower()
mot = {}
for letter in nom:
    if letter in mot:
        mot[letter] += 1
    else:
        mot[letter] = 1   

for letter in sorted(mot):
    print(f"{letter} : {mot[letter]}")
