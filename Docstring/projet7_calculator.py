while True:
    nb = int(input("un nombre entre 1 et 10: "))
    if nb in range(1, 11):  
        for i in  range(1, 11):       #Prends le premier élément de la file d'attente et mets-le dans la variable i
            ni  = nb * i 
            print(f"{nb} X {i} = {ni}")
    else:
        break
                