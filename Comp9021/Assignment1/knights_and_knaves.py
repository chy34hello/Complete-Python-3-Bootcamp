from ast import keyword
import re

question = 'Which text file do you want to use for the puzzle? '
sirs_with_sentences_unsorted = dict()
all_pissible_combination = []
sentence_divider = '\.|\?|\!'
binary_symbol = 'b'
keyword_Sir = 'Sir '
keyword_sir = 'sir '
keyword_sirs = 'Sirs '
keyword_least = 'least'
keyword_most = 'most'
keyword_knight = ' knight'
keyword_knights = ' knights'
keyword_knave = ' knave'
keyword_knaves = ' knaves'
keyword_exactly = 'exactly'
keyword_us = ' us '
keyword_are = 'are '
keyword_all = 'all '
keyword_am = 'am '
keyword_i = 'i '
keyword_I = 'I '
keyword_is = ' is '
and_operator = ' and '
or_operator = ' or '
quote = '"'
space = ' '
comma = ','
change_line = '\n'
empty_string = ''


def open_test_file():
    file_name = input(question)
    try:
        with open(file_name, 'r') as f:
            file_content = f.read()
    except FileNotFoundError:
        print(f"file not found: {file_name}")
    return file_content


def format_and_generate_list(file_content, sentence_divider):
    formated_content = file_content.replace(change_line, space).replace(
        '!"', '"!').replace('."', '".').replace(',"', '",').strip()
    divided_file_list = re.split(sentence_divider, formated_content)
    divided_file_list.pop()
    return divided_file_list


def parsing_to_dict(sir_list, sentence_divider, open_test_file, format_and_generate_list):
    converted_file_list = format_and_generate_list(
        open_test_file(), sentence_divider)
    for sentence in converted_file_list:

        if keyword_Sir in sentence and quote in sentence:

            statement = sentence.split(quote)[1]
            sentence = sentence.replace(statement, empty_string)
            name = fetch_content_after_keyword(sentence, keyword_Sir)
            speaker = name.split(space)[0]
            sir_list[speaker.strip()] = statement

            while keyword_Sir in statement:
                statement = statement.replace(comma, empty_string)
                name = fetch_content_after_keyword(statement, keyword_Sir)
                sir_involved = name.split(space)[0]
                if sir_involved.strip() not in sir_list.keys():
                    sir_list[sir_involved.strip()] = empty_string
                statement = name.replace(sir_involved, empty_string)

        elif keyword_Sir in sentence and quote not in sentence:
            sentence = sentence.replace(comma, empty_string)
            non_speaker = fetch_content_after_keyword(
                sentence, keyword_Sir).split(space)[0]

            if non_speaker.strip() not in sir_list.keys():
                sir_list[non_speaker.strip()] = empty_string

        elif keyword_sirs in sentence:
            after_keyword = fetch_content_after_keyword(sentence, keyword_sirs)
            namesList = after_keyword.split(comma)
            for name in namesList:
                if and_operator in name:
                    before, key, name = name.partition(and_operator)
                    sir_list[before.strip()] = empty_string
                    sir_list[name.strip()] = empty_string
                else:
                    sir_list[name.strip()] = empty_string
    return dict(sorted(sir_list.items()))


def fetch_content_after_keyword(sentence, keyword):
    before_key, key, after_keyword = sentence.partition(keyword)
    return after_keyword


def generate_possibilities(all_pissible_combination, sirs_with_statements):
    number_of_sirs = len(sirs_with_statements)
    formating_String = str(0)+str(number_of_sirs)+binary_symbol
    for possibility in range(2**number_of_sirs):
        temp = [(int(c)) for c in f'{possibility:{formating_String}}']
        all_pissible_combination.append(temp)


def conjunction_of_sirs(sentence):
    return True if and_operator in sentence.lower() else False


def disjunction_of_sirs(sentence):
    return True if or_operator in sentence.lower() else False


def form_one(sentence):
    least = True if keyword_least in sentence.lower() else False
    us = True if keyword_us in sentence.lower() else False
    return least and (conjunction_of_sirs(sentence.lower()) or us)


def form_two(sentence):
    most = True if keyword_most in sentence.lower() else False
    us = True if keyword_us in sentence.lower() else False
    return most and (conjunction_of_sirs(sentence.lower()) or us)


def form_three(sentence):
    exactly = True if keyword_exactly in sentence.lower() else False
    us = True if keyword_us in sentence.lower() else False
    return exactly and (conjunction_of_sirs(sentence.lower()) or us)


def form_four(sentence):
    are = True if keyword_are in sentence.lower() else False
    all = True if keyword_all in sentence.lower() else False
    return are and all


def form_five(sentence):
    am = True if keyword_am in sentence.lower() else False
    I = True if keyword_i in sentence.lower() else False
    return am and I


def form_six(sentence):
    sir = True if keyword_sir in sentence.lower() else False
    _is = True if keyword_is in sentence.lower() else False
    no_or = False if or_operator in sentence.lower() else True
    return sir and no_or and _is


def form_seven(sentence):
    _is = True if keyword_is in sentence.lower() else False
    return _is and disjunction_of_sirs(sentence.lower())


def form_eight(sentence):
    are = True if keyword_are in sentence.lower() else False
    return are and conjunction_of_sirs(sentence.lower())


def bi_conditional_check(condition_1, condition_2):
    return True if condition_1 == condition_2 else False


def identify_sir_from_statement(sentense):
    sir_list = list()
    sentense = sentense.replace(comma, empty_string)
    splited = sentense.split(space)
    for i in range(0, len(splited)):
        if splited[i].lower() == keyword_sir.strip():
            sir_list.append(splited[i+1])
    if keyword_I in sentense:
        sir_list.append(keyword_I.strip())
    return sir_list


def replace_I_with_sir(speaker, sirs_involved):
    for i in range(len(sirs_involved)):
        if sirs_involved[i] == keyword_I.strip():
            sirs_involved[i] = speaker


def is_speaker_knight(speaker, possibility):
    index_of_speaker = involved_sir_list.index(speaker)
    speaker_is_knight = True if possibility[index_of_speaker] == 1 else False
    return speaker_is_knight


def calculate_form_1(speaker, possibility, sentence):
    value = False
    speaker_is_knight = is_speaker_knight(speaker, possibility)

    if keyword_us in sentence:
        for sir in possibility:
            if keyword_knight in sentence.lower():
                value = True if sir == 1 else False
            else:
                value = True if sir == 0 else False
            return bi_conditional_check(speaker_is_knight, value)

    sirs_involved = identify_sir_from_statement(sentence)
    replace_I_with_sir(speaker, sirs_involved)

    for sir in sirs_involved:
        index = involved_sir_list.index(sir)
        if keyword_knight in sentence.lower():
            if possibility[index] == 1:
                value = True
                return bi_conditional_check(speaker_is_knight, value)
        elif keyword_knave in sentence.lower():
            if possibility[index] == 0:
                value = True
                return bi_conditional_check(speaker_is_knight, value)
    return value


def calculate_form_2(speaker, possibility, sentence):
    sir_number = 0
    speaker_is_knight = is_speaker_knight(speaker, possibility)

    if keyword_us in sentence:
        for sir in possibility:
            if keyword_knight in sentence.lower() and sir == 1:
                sir_number += 1
            elif keyword_knave in sentence.lower() and sir == 0:
                sir_number += 1
        return bi_conditional_check(speaker_is_knight, sir_number <= 1)

    sirs_involved = identify_sir_from_statement(sentence)
    replace_I_with_sir(speaker, sirs_involved)

    for sir in sirs_involved:
        index = involved_sir_list.index(sir)
        if keyword_knight in sentence.lower() and possibility[index] == 1:
            sir_number += 1
        elif keyword_knave in sentence.lower() and possibility[index] == 0:
            sir_number += 1
    return bi_conditional_check(speaker_is_knight, sir_number <= 1)


def calculate_form_3(speaker, possibility, sentence):
    sir_number = 0
    speaker_is_knight = is_speaker_knight(speaker, possibility)

    if keyword_us in sentence:
        for sir in possibility:
            if keyword_knight in sentence.lower() and sir == 1:
                sir_number += 1
            elif keyword_knave in sentence.lower() and sir == 0:
                sir_number += 1
        return bi_conditional_check(speaker_is_knight, sir_number == 1)

    sirs_involved = identify_sir_from_statement(sentence)
    replace_I_with_sir(speaker, sirs_involved)

    for sir in sirs_involved:
        index = involved_sir_list.index(sir)
        if keyword_knight in sentence.lower() and possibility[index] == 1:
            sir_number += 1
        elif keyword_knave in sentence.lower() and possibility[index] == 0:
            sir_number += 1
    return bi_conditional_check(speaker_is_knight, sir_number == 1)


def calculate_form_4(speaker, possibility, sentence):
    sir_number = 0
    speaker_is_knight = is_speaker_knight(speaker, possibility)

    if keyword_us in sentence:
        for sir in possibility:
            if keyword_knights in sentence.lower() and sir == 1:
                sir_number += 1
            elif keyword_knaves in sentence.lower() and sir == 0:
                sir_number += 1
    return bi_conditional_check(speaker_is_knight, sir_number == len(possibility))


def calculate_form_5(speaker, possibility, sentence):

    speaker_is_knight = is_speaker_knight(speaker, possibility)
    value = speaker_is_knight if keyword_knight in sentence.lower() else not speaker_is_knight
    return bi_conditional_check(speaker_is_knight, value)


def calculate_form_6(speaker, possibility, sentence):
    value = True
    speaker_is_knight = is_speaker_knight(speaker, possibility)
    sirs_involved = identify_sir_from_statement(sentence)

    for sir in sirs_involved:
        index = involved_sir_list.index(sir)
        if keyword_knight in sentence.lower():
            value = True if possibility[index] == 1 else False
        elif keyword_knave in sentence.lower():
            value = True if possibility[index] == 0 else False
    return bi_conditional_check(speaker_is_knight, value)


def calculate_form_7(speaker, possibility, sentence):
    value = False
    speaker_is_knight = is_speaker_knight(speaker, possibility)

    sirs_involved = identify_sir_from_statement(sentence)
    replace_I_with_sir(speaker, sirs_involved)

    for sir in sirs_involved:
        index = involved_sir_list.index(sir)
        if keyword_knight in sentence.lower() and possibility[index] == 1:
            value = True
        elif keyword_knave in sentence.lower() and possibility[index] == 0:
            value = True
    return bi_conditional_check(speaker_is_knight, value)


def calcualte_form_8(speaker, possibility, sentence):
    value = True
    speaker_is_knight = is_speaker_knight(speaker, possibility)

    sirs_involved = identify_sir_from_statement(sentence)
    replace_I_with_sir(speaker, sirs_involved)

    for sir in sirs_involved:
        index = involved_sir_list.index(sir)
        if keyword_knights in sentence.lower() and possibility[index] == 0:
            value = False
        elif keyword_knaves in sentence.lower() and possibility[index] == 1:
            value = False
    return bi_conditional_check(speaker_is_knight, value)


def true_false(num):
    return True if num else False


def print_final_results(finalSolutionList):
    finalString = 'The Sirs are:'
    for sir in involved_sir_list:
        finalString += ' ' + sir
    print(finalString)
    if len(finalSolutionList) == 0:
        print('There is no solution.')
    elif len(finalSolutionList) == 1:
        print('There is a unique solution:')
        for i in range(len(involved_sir_list)):
            answer = 'Knight' if finalSolutionList[0][i] == 1 else 'Knave'
            print(f'Sir {involved_sir_list[i]} is a {answer}.')
    else:
        print(f'There are {len(finalSolutionList)} solutions.')


def check_whether_all_true(result_list_temp, currentPossibility):
    for res in result_list_temp:
        if res == False:
            currentPossibility = False
    result_list_temp.clear()
    return currentPossibility


def load_data_to_memory():
    global involved_sir_list
    sirs_with_statements = parsing_to_dict(
        sirs_with_sentences_unsorted, sentence_divider, open_test_file, format_and_generate_list)
    generate_possibilities(all_pissible_combination, sirs_with_statements)
    involved_sir_list = list(sirs_with_statements.keys())
    return sirs_with_statements


def iterate_through_truthtable(final_solution_list, sirs_with_statements):
    for posibility in all_pissible_combination:
        result_list_temp = list()
        currentPossibility = True
        for i in range(len(sirs_with_statements)):
            result = False
            statement = sirs_with_statements[involved_sir_list[i]]
            data = involved_sir_list[i], posibility, statement
            if(statement):
                if form_one(statement):
                    result = calculate_form_1(*data)
                elif form_two(statement):
                    result = calculate_form_2(*data)
                elif form_three(statement):
                    result = calculate_form_3(*data)
                elif form_four(statement):
                    result = calculate_form_4(*data)
                elif form_five(statement):
                    result = calculate_form_5(*data)
                elif form_six(statement):
                    result = calculate_form_6(*data)
                elif form_seven(statement):
                    result = calculate_form_7(*data)
                elif form_eight(statement):
                    result = calcualte_form_8(*data)
                result_list_temp.append(result)

        currentPossibility = check_whether_all_true(
            result_list_temp, currentPossibility)
        if currentPossibility == True:
            final_solution_list.append(posibility)


def run():
    final_solution_list = list()
    sirs_with_statements = load_data_to_memory()
    iterate_through_truthtable(final_solution_list, sirs_with_statements)
    print_final_results(final_solution_list)


run()
