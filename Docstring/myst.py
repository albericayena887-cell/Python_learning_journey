nombre_mystere = 7

while True:
    nb = int(input("Devinez le nombre: "))
    if nb == nombre_mystere:
        print("Bien joué")
        break
    else:
        print("erreur")
print(f"{nb} est ça")        


       

    


# Demander à l'utilisateur de deviner le nombre.
# Afficher si le nombre entré par l'utilisateur est égal au nombre mystère