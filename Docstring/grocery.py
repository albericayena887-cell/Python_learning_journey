articles = {}   # dictionnaire vide au départ : va stocker "article": nombre_de_fois

while True:                     # boucle infinie : continue jusqu'à ce qu'on force l'arrêt
    try:
        ligne = input()         # demande une saisie (sans message, l'énoncé n'en montre pas)
        ligne = ligne.upper()   # met en majuscules tout de suite, insensible à la casse

        if ligne in articles:
            articles[ligne] = articles[ligne] + 1   # déjà vu : on incrémente le compteur
        else:
            articles[ligne] = 1                       # première fois : on démarre à 1

    except EOFError:            # se déclenche quand l'utilisateur appuie sur Ctrl+D
        break                   # on sort de la boucle "while True", plus rien à ajouter

# à partir d'ici, on est SORTI de la boucle : Ctrl+D a été pressé, la liste est complète

for article in sorted(articles):          # parcourt les articles dans l'ordre alphabétique
    print(articles[article], article)     # affiche : nombre, espace, nom de l'article


"""
Réfléchis à ce que fait sorted(articles)

Cette ligne parcourt tous les articles du dictionnaire, dans l'ordre alphabétique, pour les afficher.
 Mais à quel moment le dictionnaire articles est-il complet ? 
 Seulement une fois que l'utilisateur a fini de taper tous ses articles — 
c'est-à-dire seulement après que Ctrl+D ait été pressé et que la boucle se soit arrêtée.
"""    