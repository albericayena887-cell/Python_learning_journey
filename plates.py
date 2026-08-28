def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if not s[:2].isalpha():
        return False
    if not s.isalnum():
        return False

    digit_commence = False
    for c in s:
        if digit_commence:
            if not c.isdigit():
                return False
        else:
            if c.isdigit():
                if c == "0":
                    return False
                digit_commence = True

    return True


main()
"""
python
def main():
    plate = input("Plate: ")

On définit la fonction principale. Elle demande une plaque d'immatriculation à l'utilisateur et la stocke dans plate.

python
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

On appelle is_valid(plate), qui va renvoyer soit True, soit False. Si elle renvoie True, on affiche "Valid". Sinon, "Invalid".

python
def is_valid(s):

On définit une deuxième fonction, is_valid, qui reçoit un texte s (la plaque à vérifier) et va renvoyer True ou False selon qu'elle respecte toutes les règles.

python
    if len(s) < 2 or len(s) > 6:
        return False

Première règle : la longueur. Si s a moins de 2 caractères ou plus de 6 caractères, elle est trop courte ou trop longue → on arrête immédiatement et on renvoie False. Si cette ligne ne se déclenche pas, ça veut dire que la longueur est correcte (entre 2 et 6 inclus), et le code continue vers la suite.

python
    if not s[:2].isalpha():
        return False

Deuxième règle : les 2 premiers caractères doivent être des lettres. s[:2] prend les 2 premiers caractères de s. .isalpha() vérifie que ce sont bien des lettres (True si oui). not inverse ça : si ce n'est pas le cas (donc au moins un des deux premiers caractères n'est pas une lettre), on renvoie False.

python
    if not s.isalnum():
        return False

Troisième règle : aucun caractère interdit. .isalnum() vérifie que s entier ne contient que des lettres et/ou des chiffres. Si not de ça est vrai (donc s contient autre chose, comme un point ou un espace), on renvoie False.

python
    digit_commence = False

On crée une variable "mémoire" qui vaut False au départ : elle va nous servir à savoir, à chaque instant de la boucle qui suit, si on a déjà croisé un chiffre ou non.

python
    for c in s:

On démarre une boucle qui va examiner chaque caractère de s, un par un, en les stockant tour à tour dans c.

python
        if digit_commence:

On teste : est-ce qu'on a déjà vu un chiffre avant, dans un tour précédent de cette même boucle ?

python
            if not c.isdigit():
                return False

Si oui (on est censé être dans la "zone des chiffres" désormais), alors le caractère actuel c doit être un chiffre. Si ce n'est pas le cas (not c.isdigit() est vrai), ça veut dire qu'une lettre est apparue après un chiffre — ce qui est interdit → on renvoie False.

python
        else:
            if c.isdigit():

Sinon (on n'a pas encore vu de chiffre jusqu'ici), on vérifie si le caractère actuel c est justement un chiffre — ce serait alors le tout premier chiffre rencontré.

python
                if c == "0":
                    return False

Si c'est le cas, on vérifie une règle supplémentaire : ce premier chiffre ne doit pas être "0". Si c'est "0", on renvoie False.

python
                digit_commence = True

Si le premier chiffre n'était pas "0", tout va bien pour l'instant — on met à jour notre mémoire : digit_commence devient True, pour que les prochains tours de boucle sachent qu'on est maintenant dans la "zone des chiffres" et doivent vérifier chaque caractère suivant en conséquence.

python
    return True

Cette ligne n'est pas indentée dans la boucle for — elle s'exécute donc seulement une fois la boucle entièrement terminée (tous les caractères examinés sans qu'aucun return False ne se soit déclenché). Ça veut dire que toutes les règles ont été respectées → on renvoie True.

python
main()

On lance le programme en appelant main().

Une question pour vérifier ta compréhension : pourquoi return True doit-il être placé après la boucle for (donc à la même indentation que digit_commence = False), et pas à l'intérieur de la boucle ?

"""