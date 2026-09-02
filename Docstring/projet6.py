total = 0
compteur = 0            # on initialise à 0
while True:
    num = int(input("Nombre: ")) # on le met dedans pour que le num  = number reapparaisse pour qu'on retape un autre nombre 
    if num == 0:    
        break
    total = total + num             #chaque fois qu'un utilisateur vous donne une bille (un nombre), on ajoute ça au total
    compteur = compteur + 1         #chaque fois qu'un utilisateur vous donne une bille (un nombre), on ajoute ça au compteur
mo = total/compteur
print(f"Total: {total}") 
print(f"Moyenne: {mo}")
    