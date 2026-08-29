def get_vowels_numbers(mot):
    compt = 0
    for c in mot:
        if c in "aeiouAEIOU":
            compt+=1
    return compt        
nom = input("entrez un  mot: ")
print(get_vowels_numbers(nom))