from app.models import Word


def test():
    word = Word.objects.all()
    print(list(word.values()))

