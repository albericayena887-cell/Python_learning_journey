numbers = [1, 2, 3, 4, 5]
resultat = [ (num, "even")  if num % 2 == 0 else (num, "odd")  for  num in numbers] #  num in range(24) aussi marche bien
print(resultat)