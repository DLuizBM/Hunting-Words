# Importar da raiz
from app.models import Word

words_in_db = Word.objects.all()
words = list(words_in_db.values())

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letters_with_accent = "áéçãíâú"
one_point = ("EAIONRTLSU", 1)
two_points = ("DG", 2)
three_points = ("BCMP", 3)
five_points = ("FHV", 5)
eigth_points = ("JX", 8)
thirteen_points = ("QZ", 13)
