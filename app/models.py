from django.db import models

my_error_messages = {
    'unique': 'Essa palavra já foi inserida.'
}


class Word(models.Model):
    word = models.CharField('Nova Palavra', max_length=20, unique=True, error_messages=my_error_messages)
    # blank=True, não obriga que o campo seja preeenchido no formulário.
    # a validação de um formulário permitirá a entrada de um valor vazio
    # This field is required, essa mensagem não aparece quando blank=true

    class Meta:
        verbose_name = "Novas Palavras"
        verbose_name_plural = "Caça Palavras"

    def __str__(self):
        return self.word
    """
    Com o __str__, a formatação ao salvar um objeto fica assim:
    The word “Carro” was added successfully.
    Sem o __str__, não é mostrada a palavra e sim object
    The word “object” was added successfully.
    """
