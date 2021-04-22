import Base


def multiple_words(input_letters, position=0):
    letters = list(input_letters)
    multiple_words_with_score = {}
    while letters:
        data = Base.base("".join(letters), position)
        if 'best_word' in data.keys():
            multiple_words_with_score.update({data['best_word']: data['score']})
            for letter in data['best_word'].lower():
                letters.remove(letter)
        elif 'message' in data.keys() and not len(multiple_words_with_score):
            multiple_words_with_score.update(data)
            break
        else:
            break
    return multiple_words_with_score, letters




