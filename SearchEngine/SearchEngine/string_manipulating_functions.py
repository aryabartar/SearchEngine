def remove_ha(string):
    if len(string) > 2:
        if string[len(string) - 2: len(string) + 1] == "ها":
            string = string[0:len(string) - 2]
    return string


def remove_aan(string, all_tokens_set):
    if len(string) > 2:
        if string[0:len(string) - 2] in all_tokens_set and string[len(string) - 2: len(string) + 1] == "ان":
            new_string = string[0:len(string) - 2]
            string = new_string
    return string


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


def manipulate_query(query, all_tokens_set, COMBINATIONAL_WORDS):
    query = string_combination_connector(query, COMBINATIONAL_WORDS)
    words_list = query.split(" ")

    for i, word in enumerate(words_list):
        words_list[i] = remove_ha(word)
        words_list[i] = remove_aan(words_list[i], all_tokens_set)

    result_query = ""

    for item in words_list:
        result_query += item
        result_query += " "

    return result_query


# for user input
def string_combination_connector(user_input, COMBINATIONAL_WORDS):
    result_list = combination_connector(user_input.split(" "), COMBINATIONAL_WORDS)
    result_str = ""
    for item in result_list:
        result_str += item
        result_str += " "

    return result_str

