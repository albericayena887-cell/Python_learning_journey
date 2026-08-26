words = ['sky', 'apple', 'rhythm', 'fly', 'orange']
for word in words:
    for letter in word:
        if letter.lower() in "aeoiu":
            print(f"{word} contains the woyel {letter}")
            break
        else:
            print(f"{word} contains No woyel ")
            break    