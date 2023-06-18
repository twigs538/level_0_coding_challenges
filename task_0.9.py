def vowels(string):
    vowels_found = ""
    delimiter = ", "
    string_lower = string.lower()

    for letter in string_lower:
        if letter in "aeiou" and letter not in vowels_found:
            vowels_found += letter

    result = delimiter.join(vowels_found)
    print(f"Vowels: {result}")

if __name__ == '__main__':
    vowels("Umuzi")