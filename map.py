celsius = [0, 10, 20, 30, 40]

def to_fah(temp):
    return (temp * 9/5) + 32
res = list(map(to_fah, celsius))
print(res)