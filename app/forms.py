from django import forms
from django.forms import Field
from .models import Word
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
# ugettext_lazy, django translate function

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# Desafio: Fazer validação com o formulário nativo do html (resolvido)


class WordModelForm(forms.ModelForm):
    def clean_word(self):
        """
        Para fazer a validação de um atributo isolado, deve-se usar a seguinte sintaxe para a função:
        def clean_atributo, nesse caso o atributo é "word", que é o mesmo em data = self.cleaned_data['word']
        e que deve ser um dos campos do formulário. Se fosse colocado por exemplo, def clean_validate_word
        não iria funcionar, pois validate_word não é uma campo válido no formulário. Para validar vários campos
        na mesma função, basta usar apenas def clean(self):
        """
        data = self.cleaned_data['word']
        for letter in data:
            if letter.lower() not in alphabet.lower():
                raise ValidationError(_('Apenas letras são aceitas'))
                # self._errors['word'] = self.error_class(["Apenas letras são aceitas."])
        return data

    class Meta:
        model = Word
        fields = ['word']
        # labels = {'word': _("Insira uma nova palavra.")}
        # help_texts = {'word': _("Ex: Casa")}
        # para mudar a mensagem This Field is required.
        Field.default_error_messages = {'required': "O campo não pode ser vazio."}