# Password Generation Tool

from itertools import product

def green(text: str) -> str:
    """Returns the given text wrapped in ANSI escape codes for green color."""
    return f"\033[92m{text}\033[0m"

def pwgen():
    """Generate passwords based on user input and save to a file."""

    words       = ['']
    numbers     = ['']
    specials    = ['!', '@', '#', '$', '%', '&']
    separators  = ['', '_', '-', '.']

    # Accept words input and append to list
    words_input = input(green("Enter word(s)/letter(s) separated by commas (or press Enter to skip): ")).strip()
    if words_input:
        words += [w.strip() for w in words_input.split(',') if w.strip()]

    # Accept numbers input and append to list
    num_input = input(green("Enter number(s) separated by commas (or press Enter to skip): ")).strip()
    if num_input:
        numbers += [n.strip() for n in num_input.split(',') if n.strip()]

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

    print(green(f"Done! {count * 4} passwords saved to passwords.txt"))
    return
