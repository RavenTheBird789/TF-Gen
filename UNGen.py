# Username Generation Tool

from itertools import product

def variants(word):
    return [word, word.capitalize(), word.upper()]

names = [''] # Type name(s) here 
roles = [''] # Type role(s) here
separators = ['', '_', '-']

count = 0

with open('usernames.txt', 'w') as f:
    for n, r, sep in product(names, roles, separators):
        for nv, rv in product(variants(n), variants(r)):
            f.write(f"{nv}{sep}{rv}\n");
            count += 1

print(f"Done! {count} usernames saved to usernames.txt")