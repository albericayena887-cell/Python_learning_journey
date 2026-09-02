ner = map(int, input("Un texte: ").split(" ")) ## très très important

"""
for i in ner:
    # Si le nombre est impair, on passe directement au tour suivant
    if i % 2 != 0:
        continue
    ;
"""

for i in ner:
    if i % 2 == 0:
        print(i)