def main():
    x = int(input("Entrez x : "))
    if is_even(x):
        print("x est un nombre pair")
    else:
        print("x est un nombre impair")


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
main()    


"""
  si on voulait que ce soit plus simple

  
def main():
    x = int(input("Entrez x : "))
    if x % 2 == 0:
        print("x est un nombre pair")
    else:
        print("x est un nombre impair")
"""
