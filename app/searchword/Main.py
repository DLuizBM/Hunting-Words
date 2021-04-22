'''

Para a melhor organização e visualização do código e da explicação da lógica de funcionamento,
a explicação está no arquivo LogicaDefuncionamento.pdf. Leia também o arquivo ReadMe.md para
compreender como executar o código.

'''
import PositionBonus
import ServiceWords

while 1:
    input_letters = input("Digite as letras disponíveis nesta jogada: ")
    try:
        position_input = int(input("Digite a posição: "))
        correct_index = input_letters.__getitem__(position_input - 1)
        data = PositionBonus.position_bonus(ServiceWords.treat_letter(input_letters.lower()), position_input)
        ServiceWords.format_output(data)
    except ValueError:
        print("A posição deve ser um valor inteiro.")
    except IndexError:
        print("A posição escolhida é maior do que o tamanho da palavra.")