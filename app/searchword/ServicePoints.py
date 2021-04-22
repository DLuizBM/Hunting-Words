# Importar da raiz
from app.searchword import Repository


def best_play(all_score_dict):
    max_score = max(all_score_dict.values())
    list_of_best_keys = list(filter(lambda key: all_score_dict[key] == max_score, all_score_dict.keys()))
    best_words = {key: all_score_dict[key] for key in list_of_best_keys}
    return best_words


def points_for_letter(letter):
    letter_score = 0
    if letter in Repository.one_point[0].lower():
        letter_score += Repository.one_point[1]
    elif letter in Repository.two_points[0].lower():
        letter_score += Repository.two_points[1]
    elif letter in Repository.three_points[0].lower():
        letter_score += Repository.three_points[1]
    elif letter in Repository.five_points[0].lower():
        letter_score += Repository.five_points[1]
    elif letter in Repository.eigth_points[0].lower():
        letter_score += Repository.eigth_points[1]
    elif letter in Repository.thirteen_points[0].lower():
        letter_score += Repository.thirteen_points[1]
    else:
        raise ValueError
    return letter_score


def get_all_scores(final_words, position=0):
    all_score_dict = {}
    for word in final_words:
        word_score = 0
        for letter in word:
            if position > 0 and word.index(letter) == (position - 1):
                word_score += points_for_letter(letter) * 2
            else:
                word_score += points_for_letter(letter)
        all_score_dict.update({word: word_score})
    return all_score_dict

