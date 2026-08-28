ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort(reverse=False)
#print(ages)
minim = min(ages)
maxim = max(ages)
#print(maxim)
ages.append(minim)
ages.append(maxim)
#print(ages)
ages.sort(reverse=False)
print(ages)

