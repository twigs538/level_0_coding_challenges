def vowels(string):
    vowels_found = ""
    delimeter = ", "
    string_lower = string.lower()

    for letter in string_lower:
        if letter in "aeiou":
            if letter in vowels_found:
                continue
            vowels_found = vowels_found + letter
    result = delimeter.join(vowels_found)
    print(f"Vowels: {result}")

if __name__ == '__main__':
    vowels("Umuzi")