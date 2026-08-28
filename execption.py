while True:
    try:
        x = int(input("Entrez un nombre: "))
    except ValueError:                 # Si il y a ValueError , 
        print("x is not an integer")   # Tu mets ça 
    else:                              # le else est pour montrer que si il n'y a pas de value error,
        break                          # il break , donc il sort de la boucle while pour aller à la ligne
print(f"{x} is an integer")            