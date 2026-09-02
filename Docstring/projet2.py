total = 0            # on initialise à 0
while True:
    num = int(input("Nombre: ")) # on le met dedans pour que le num  = number reapparaisse pour qu'on retape un autre nombre 
    if num == 0:    
        break
    total = total + num
print(f"Total: {total}")    
    