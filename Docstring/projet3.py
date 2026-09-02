while True:
    try:
        x = int(input("Ton age: "))
        if x > 0:
            break
    except ValueError:
        print("Retape ")
print(f"Âge enregistré : {x}")        