def max(a, b):
    if a > b:
        return a
    else:
        return b

first = int(input("Entrez la première valeur: "))    
last = int(input("Entrez la deuxième valeur: "))    
maxi = max(first, last)
print(f"La plus grande valeure est {maxi} ")