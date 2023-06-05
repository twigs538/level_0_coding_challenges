def vowels(string):
    vowels_found = ""
    delimeter = ", "
    lower_case = string.lower()

    for letter in lower_case:
        if letter in "aeiou":
            if letter in vowels_found:
                continue
            vowels_found = vowels_found + letter
    result = delimeter.join(vowels_found)
    print(f"Vowels: {result}")

vowels("Umuzi")