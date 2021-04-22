from django.shortcuts import render
from .models import Word
from .forms import WordModelForm
from app.searchword.Base import base_input
# quando se utiliza um pacote externo, deve-se colocar todo o caminho desde a raiz
# nesse caso, começa em app


def index(request):
    return render(request, 'index.html')


def service_view(request):
    if request.method == "POST":
        form = WordModelForm(request.POST or None)
        if form.is_valid():
            form.save()
            form = WordModelForm()
        context = {
            'form': form
        }
        return render(request, 'index.html', context)
    elif request.method == "GET":
        word = Word.objects.all()
        print(base_input("dica"))
        context = {
            'words': word
        }
        return render(request, 'words.html', context)

