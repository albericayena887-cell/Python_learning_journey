def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b
def operation(x, y, f):
    return f(x, y)
resultat = operation(5, 9, addition)
print(resultat)