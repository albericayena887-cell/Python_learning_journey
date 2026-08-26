"""
words = [0, 10, 20, 30, 40]
def conv(word):
    return word > 4
vec = list(filter(conv, words))
print(vec)
"""


words = ['arbre', 'ciel', 'montagne', 'riviere']
def conv(word):
    return len(word) > 4
vec = list(filter(conv, words))
print(vec)

