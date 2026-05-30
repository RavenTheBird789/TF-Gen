# Username Generation Tool

from itertools import product

def green(text: str) -> str:
    """Returns the given text wrapped in ANSI escape codes for green color."""
    return f"\033[92m{text}\033[0m"

def ungen():
    def variants(word):
        return [word, word.capitalize(), word.upper()]

    names = [''] # Type name(s) here 
    roles = [''] # Type role(s) here
    specials    = ['!', '@', '#', '$', '%', '&']
    separators = ['', '_', '-']

    # Accept names input and append to list
    names_input = input(green("Enter a name or names separated by commas (or press Enter to skip): ")).strip()
    if names_input:
        names += [n.strip() for n in names_input.split(',') if n.strip()]

    # Accept roles input and append to list
    roles_input = input(green("Enter a role or roles separated by commas (or press Enter to skip): ")).strip()
    if roles_input:
        roles += [r.strip() for r in roles_input.split(',') if r.strip()]

    count = 0

    with open('usernames.txt', 'w') as f:
        for n, r, sep, sp in product(names, roles, separators, specials):
            for nv, rv in product(variants(n), variants(r)):
                for nv in variants(n):
                    f.write(f"{nv}{sep}{rv}\n")
                    f.write(f"{nv}{sep}{n}{sp}\n")
                    f.write(f"{sp}{nv}{sep}{n}\n")
                    f.write(f"{nv}{sp}{n}\n")
                    f.write(f"{n}{sep}{nv}{sp}\n")
                    count += 1

    print(green(f"Done! {count * 5} usernames saved to usernames.txt"))
    return
