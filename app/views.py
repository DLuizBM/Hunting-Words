from django.shortcuts import render, HttpResponse
from .models import Word
from .forms import WordModelForm
import json
from app.searchword.Base import base_input
# quando se utiliza um pacote externo, deve-se colocar todo o caminho desde a raiz
# nesse caso, começa em app


def index(request):
    if request.method == "POST":
        print("Post")
        print(request.body)
        body = json.loads(request.body) # deserializa o request.body em um objeto python ou outro tipo, dependendo
                                        # do que é enviado, consultar a tabela de conversão do loads
        print(body)
        print(base_input(body.get('caracteres')))
        return HttpResponse(body)
    """
    https://stackoverflow.com/questions/25791913/querydict-always-empty-from-ajax-post
    request.body = django não desserializa JSON payloads(o que é útil do que é transmitido) por si só, request.POST é para dados
    enviados por post do form html. request.body pega toda a transmissão, mas o programador deve desserializar a informação
    request.POST traz <QueryDict: {}>, pois não desserializa a informação
    request.body traz b'informação', que é uma bytestring, usada para imagens binárias, por exemplo.
    
    """
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

