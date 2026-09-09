"""
twt = input("Input: ")
for c in twt:
    if c in ["a", "e", "o", "i", "u", "A", "E", "I", "U", "O"]:
        twt = twt.replace(c, "")
    else:
        twt = twt

print(f"Output: {twt}")

"""
def main():
    twt = input("Input: ")
    print("Output:", shorten(twt))


def shorten(word):
    resultat = ""
    for c in word:
        if c not in  "aeiouAEIOU":
            resultat += c        
    return resultat

if __name__ == "__main__":
    main()