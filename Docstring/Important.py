"""
Le continue

Comme vu juste avant : dès que Python exécute continue, il arrête immédiatement ce tour de la boucle while True et 
repart directement au début de la boucle — donc il retourne demander une nouvelle saisie (input("Fraction: ")), 
sans exécuter le reste du code qui suit dans le try

"Le break" est maintenant à l'intérieur du try, 
juste après l'affichage du résultat, avec la même indentation que les autres lignes du try —
 il ne s'exécute donc que si on arrive jusque-là, c'est-à-dire seulement quand tout s'est bien passé

 En le mettant à l'intérieur du try, juste après l'affichage du résultat, le break ne s'exécute que si on est arrivé jusque-là sans erreur — 
 c'est-à-dire seulement après une saisie réussie et un affichage réussi. Si une exception se produit avant (à cause de int(...) ou de la division), 
 Python saute directement au except et ne passe jamais par le break — la boucle continue donc naturellement.


"""

while True:
    try:
        x, y = map(int, input("Fraction: ").split("/"))

        if x < 0 or y <= 0 or x > y:
            continue    

        pourcentage = round((x / y) * 100)

        if pourcentage <= 1:
            print("E")
        elif pourcentage >= 99:
            print("F")
        else:
            print(f"{pourcentage}%")

        break

    except (ValueError, ZeroDivisionError):
        print("Veuillez entrer une fraction valide")