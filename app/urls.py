from .views import service_view, index, possible_words
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('words', service_view, name='words'),
    path('possible_words', possible_words, name='possible_words'),
]
'''
 Como o GET e o POST estão na mesma view, só é necessário uma URL. Pois
 é pela requisição que saberemos qual método está sendo utilizado e em 
 qual condição da view service_view entrar.
 '''
