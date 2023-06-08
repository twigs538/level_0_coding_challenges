def vowels(string):
    vowels_found = set()

    for letter in string.lower():
        if letter in "aeiou":
            vowels_found.add(letter)

    result = ", ".join(vowels_found)
    print(f"Vowels: {result}")

if __name__ == '__main__':
    vowels("Umuzi")