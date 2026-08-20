def main():
    # Demande le prix du repas à l'utilisateur (ex: "$50.00"), sous forme de texte
    entree_dollars = input("How much was the meal? ")
    # Convertit ce texte en nombre décimal utilisable (ex: 50.0)
    dollars = dollars_to_float(entree_dollars)

    # Demande le pourcentage de pourboire souhaité (ex: "15%"), sous forme de texte
    entree_percent = input("What percentage would you like to tip? ")
    # Convertit ce texte en nombre décimal utilisable (ex: 0.15)
    percent = percent_to_float(entree_percent)

    # Calcule le montant du pourboire (prix du repas x pourcentage)
    tip = dollars * percent

    # Arrondit le résultat à 2 chiffres après la virgule (ex: 7.5 -> 7.50)
    tip_arrondi = round(tip, 2)
    # Affiche le résultat final, précédé d'un symbole $
    print("Leave $" + str(tip_arrondi))


def dollars_to_float(d):
    # Retire le symbole $ du texte reçu (ex: "$50.00" -> "50.00")
    sans_dollar = d.replace("$", "")
    # Convertit ce texte en nombre décimal (ex: "50.00" -> 50.0)
    nombre = float(sans_dollar)
    # Renvoie ce nombre à la fonction qui a appelé dollars_to_float
    return nombre


def percent_to_float(p):
    # Retire le symbole % du texte reçu (ex: "15%" -> "15")
    sans_pourcent = p.replace("%", "")
    # Convertit ce texte en nombre décimal (ex: "15" -> 15.0)
    nombre = float(sans_pourcent)
    # Divise par 100 pour obtenir un pourcentage utilisable dans un calcul (ex: 15.0 -> 0.15)
    resultat = nombre / 100
    # Renvoie ce nombre à la fonction qui a appelé percent_to_float
    return resultat


# Lance le programme en appelant la fonction main, définie plus haut
main()