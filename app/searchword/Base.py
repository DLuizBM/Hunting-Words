# Importar da raiz
from app.searchword import ServiceWords
from app.searchword import ServicePoints


def base_input(input_letters):
    treated_input = ServiceWords.treat_letter(input_letters.lower())
    list_of_words = ServiceWords.search_words(treated_input)
    final_words = ServiceWords.search_by_keys(treated_input, list_of_words)
    return final_words, treated_input


def base(input_letters, position=0):
    final_words, treated_input = base_input(input_letters)
    try:
        all_score = ServicePoints.get_all_scores(final_words, position)
        best_words = ServicePoints.best_play(all_score)
        if len(best_words) > 1:
            sort_by_alphabet = ServiceWords.sort_by_alphabetical_order(list(best_words))
            sort_by_length = ServiceWords.sort_by_length(sort_by_alphabet)
            best_word = sort_by_length[0]
            not_used_letter = ServiceWords.not_used_letter(treated_input, best_word)
            return {'best_word': best_word.upper(), 'score': best_words[sort_by_length[0]], 'not_used_letter': not_used_letter}
        else:
            key = best_words.keys()
            value = best_words.values()
            not_used_letter = ServiceWords.not_used_letter(treated_input, best_words)
            return {'best_word': list(key)[0].upper(), 'score': list(value)[0], 'not_used_letter': not_used_letter}

    except ValueError:
        return {'message': "\nNenhum palavra encontrada"}

