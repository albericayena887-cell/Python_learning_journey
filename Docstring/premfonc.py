def years(age):  
    if age > 18:
        return "T'es majeur"
    elif age < 18:
        return "T'es toujours mineur"               #print
    else:
        return "T'as 18 ans"                         #print
x = int(input("vb: "))          
print(years(x))                                      #years(x)