# Password Generation Tool

from itertools import product

words       = [''] # Type word(s) and/or letter(s) here
numbers     = [''] # Type number(s) here
specials    = ['!', '@', '#', '$', '%', '&']
separators  = ['', '_', '-', '.']

def variants(word):
    """Return lowercase, Capitalized, UPPER, and l33tspeak versions of a word."""
    leet_map = str.maketrans('aeiost', '4310$7')
    return [
        word,
        word.capitalize(),
        word.upper(),
        word.lower().translate(leet_map)
    ]

count = 0

with open('passwords.txt', 'w') as f:
    for w, n, sep, sp in product(words, numbers, separators, specials):
        for wv in variants(w):
            f.write(f"{wv}{sep}{n}{sp}\n")
            f.write(f"{sp}{wv}{sep}{n}\n")
            f.write(f"{wv}{sp}{n}\n")
            f.write(f"{n}{sep}{wv}{sp}\n")
            count += 1

print(f"Done! {count * 4} passwords saved to passwords.txt")