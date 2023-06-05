def common_letters(string_1, string_2):
    lower_case_string_1 = string_1.lower()
    lower_case_string_2 = string_2.lower()
    common_characters = []
    delimeter = ", "

    for letter in lower_case_string_2:
        if letter in lower_case_string_1:
            if letter in common_characters:
                continue
            common_characters = common_characters + [letter]
    results = delimeter.join(common_characters)
    return f"Common letter: {results}"

print(common_letters("house", "computers"))