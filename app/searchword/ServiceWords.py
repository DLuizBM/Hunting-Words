# Importar da raiz
from app.searchword import Repository
from collections import Counter


def treat_letter(letters):
    new_letters = ""
    for letter in letters:
        if letter in Repository.letters_with_accent:
            if letter == 'á' or letter == 'ã' or letter == 'â':
                new_letters += 'a'
            elif letter == 'é':
                new_letters += 'e'
            elif letter == 'ç':
                new_letters += 'c'
            elif letter == 'í':
                new_letters += 'i'
            elif letter == 'ú':
                new_letters += 'u'
        else:
            new_letters += letter
    return new_letters.lower()


def is_there_all_letter(treated_word, treated_input):
    is_there_all = []
    for letter_word in treated_word:
        if letter_word in treated_input:
            is_there_all.append(True)
        else:
            is_there_all.append(False)
    if all(is_there_all) and len(is_there_all) > 0:
        return True
    else:
        return False


def search_words(input_characters):
    list_of_word = []
    treated_input = treat_letter(input_characters.lower())
    for word in Repository.words:
        if len(word['word']) <= len(treated_input):
            treated_word = treat_letter(word['word'].lower())
            if is_there_all_letter(treated_word, treated_input):
                list_of_word.append(treated_word)
    return list_of_word


def is_there_all_keys(input_dict, word_dict):
    is_there_all = []
    for key in word_dict.keys():
        if input_dict[key] >= word_dict[key]:
            is_there_all.append(True)
        else:
            is_there_all.append(False)
    if all(is_there_all) and len(is_there_all) > 0:
        return True
    else:
        return False


def search_by_keys(input_characters, list_of_words):
    input_dict = dict(Counter(input_characters))
    list_of_final_words = []
    for word in list_of_words:
        word_dict = dict(Counter(word))
        if is_there_all_keys(input_dict, word_dict):
            list_of_final_words.append(word)
    return list_of_final_words


def sort_by_length(list_of_words):
    list_of_words.sort(key=lambda word: len(word))
    return list_of_words


def sort_by_alphabetical_order(list_of_words):
    list_of_words.sort(key=lambda word: word)
    return list_of_words


def not_used_letter(input_characters, best_words):
    all_letters_used = set("".join(best_words))
    input_characters = set(input_characters)
    not_used = input_characters.difference(all_letters_used)
    return "".join(not_used).upper()


def format_not_used_letters(letters):
    letters = set(letters)
    letters = list(letters)
    no_used_letter = [letter + ', ' if letters.index(letter) + 1 != len(letters) else letter + ' ' for letter in letters]
    return "".join(no_used_letter)


def format_output(data):
    information = ""
    if 'message' not in data[0].keys():
        for word in data[0].keys():
            information += word + ', '
        information += f'total de {sum(data[0].values())} pontos'
        if data[1]:
            information += f'\nSobraram: {format_not_used_letters(data[1]).upper()}'
        print(f'\n{information}')
    else:
        information = data[0].get('message')
        print(f'{information}\nSobraram: {format_not_used_letters(data[1]).upper()}')