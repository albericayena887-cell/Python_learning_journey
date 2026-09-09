def main():
    x = int(input("Entrez un nombre: "))
    print(f"Le carré de {x} vaut:{square(x)}")

def square(n):
    return n*n

if __name__ == "__main__":
    main()

