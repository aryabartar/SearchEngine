def remove_haye(string):
    if len(string) > 3:
        if string[len(string) - 3: len(string) + 1] == "های":
            string = string[0:len(string) - 3]
    return string


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


def remove_ye(string, all_tokens_set):
    # if len(string) > 2:
    #     if string[0:len(string) - 1] in all_tokens_set and string[len(string) - 1: len(string) + 1] == "ی":
    #         new_string = string[0:len(string) - 1]
    #         string = new_string
    return string


def remove_tarin(string, all_tokens_set):
    if len(string) > 4:
        if string[0:len(string) - 4] in all_tokens_set and string[len(string) - 4: len(string) + 1] == "ترین":
            new_string = string[0:len(string) - 4]
            string = new_string
    return string


def remove_tar(string, all_tokens_set):
    if len(string) > 2:
        if string[0:len(string) - 2] in all_tokens_set and string[len(string) - 2: len(string) + 1] == "تر":
            new_string = string[0:len(string) - 2]
            string = new_string
    return string


def remove_shenase(string, all_tokens_set):
    if len(string) > 2:
        if string[0:len(string) - 1] in all_tokens_set and string[len(string) - 1: len(string) + 1] == "م":
            new_string = string[0:len(string) - 1]
            string = new_string
        if string[0:len(string) - 1] in all_tokens_set and string[len(string) - 1: len(string) + 1] == "ت":
            new_string = string[0:len(string) - 1]
            string = new_string
        elif string[0:len(string) - 1] in all_tokens_set and string[len(string) - 1: len(string) + 1] == "ش":
            new_string = string[0:len(string) - 1]
            string = new_string
        elif string[0:len(string) - 3] in all_tokens_set and string[len(string) - 3: len(string) + 1] == "مان":
            new_string = string[0:len(string) - 3]
            string = new_string
        elif string[0:len(string) - 3] in all_tokens_set and string[len(string) - 3: len(string) + 1] == "تان":
            new_string = string[0:len(string) - 3]
            string = new_string
        elif string[0:len(string) - 3] in all_tokens_set and string[len(string) - 3: len(string) + 1] == "شان":
            new_string = string[0:len(string) - 3]
            string = new_string
    return string


def remove_shenase_fel_mazi_mozare(string, all_tokens_set):
    # if len(string) > 2:
    #     if string[0:len(string) - 2] in all_tokens_set and string[len(string) - 2: len(string) + 1] == "یم":
    #         new_string = string[0:len(string) - 2]
    #         string = new_string
    #     elif string[0:len(string) - 2] in all_tokens_set and string[len(string) - 2: len(string) + 1] == "ید":
    #         new_string = string[0:len(string) - 2]
    #         string = new_string
    #     elif string[0:len(string) - 2] in all_tokens_set and string[len(string) - 2: len(string) + 1] == "ند":
    #         new_string = string[0:len(string) - 2]
    #         string = new_string
    #     elif string[0:len(string) - 1] in all_tokens_set and string[len(string) - 1: len(string) + 1] == "م":
    #         new_string = string[0:len(string) - 1]
    #         string = new_string
    #     elif string[0:len(string) - 1] in all_tokens_set and string[len(string) - 1: len(string) + 1] == "ی":
    #         new_string = string[0:len(string) - 1]
    #         string = new_string
    #     elif string[0:len(string) - 1] in all_tokens_set and string[len(string) - 1: len(string) + 1] == "د":
    #         new_string = string[0:len(string) - 1]
    #         string = new_string

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
        words_list[i] = remove_haye(word)
        words_list[i] = remove_ha(word)
        words_list[i] = remove_aan(words_list[i], all_tokens_set)
        words_list[i] = remove_ye(words_list[i], all_tokens_set)
        words_list[i] = remove_tarin(words_list[i], all_tokens_set)
        words_list[i] = remove_tar(words_list[i], all_tokens_set)
        words_list[i] = remove_shenase(words_list[i], all_tokens_set)
        words_list[i] = remove_shenase_fel_mazi_mozare(words_list[i], all_tokens_set)

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
