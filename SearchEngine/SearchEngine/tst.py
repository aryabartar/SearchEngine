COMBINATIONAL_WORDS = ['عن قریب', 'من جمله', 'فی ذلک', 'مع هذا', 'علی حده', 'فی مابین']


def combination_connector(content_token_list, COMBINATIONAL_WORDS):
    def remove_space_from_string(string):
        return string.replace(" ", "")

    for combinational_word in COMBINATIONAL_WORDS:
        combinational_words_list = combinational_word.split(" ")

        j = 0

        try:
            i = content_token_list.index(combinational_words_list[j])
            initial_i = i
        except ValueError as verr:
            continue

        found = True
        while j < len(combinational_words_list):
            if combinational_words_list[j] != content_token_list[i]:
                found = False
            j += 1
            i += 1

        if found:
            content_token_list[initial_i] = remove_space_from_string(combinational_word)
            for _ in range(len(combinational_words_list) - 1):
                content_token_list.pop(initial_i + 1)

    return content_token_list


# for user input
def string_combination_connector(user_input, COMBINATIONAL_WORDS):
    result_list = combination_connector(user_input.split(" "), COMBINATIONAL_WORDS)
    result_str = ""
    for item in result_list:
        result_str += item
        result_str += " "

    return result_str


print(string_combination_connector("من فی مابین سلام", COMBINATIONAL_WORDS))
