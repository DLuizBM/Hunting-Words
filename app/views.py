from django.shortcuts import render, HttpResponse
from .models import Word
from .forms import WordModelForm
from app.searchword.Base import base_input
# quando se utiliza um pacote externo, deve-se colocar todo o caminho desde a raiz
# nesse caso, começa em app


def index(request):
    if request.method == "POST":
        print("Post")
        print(request.POST.get('input'))
        context = {
            'form': 'dica'
        }
        return HttpResponse(context)
    '''
    render, envia/renderiza a página html, ou seja, o código html, fazendo com que a página
    seja mostrada para o usuário. 
    Um acontecimento estranho estava acontecendo quando era feito um post com AJAX, em index.js
    ao fazer o POST, a página estava sendo duplicada, isso ocorria pois a linha
    document.getElementById("words").innerHTML = xhttp.responseText;
    recebia o render como resposta. Como o render mandava toda a página html, a linha do javascript
    pegava toda a página html e colocava no parágrafo de id "words", renderizando nesse parágrafo
    a página toda, navamente.
    '''
    print(request.GET)
    return render(request, 'index.html')


def possible_words(request):
    if request.method == "GET":
        print(request.GET.get('caracters'))
        caracters = request.GET.get('caracters')
        return HttpResponse('olá')


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
        context = {
            'words': word
        }
        return render(request, 'words.html', context)

