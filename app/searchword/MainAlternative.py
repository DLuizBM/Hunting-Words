"""
Para a melhor organização e visualização do código e da explicação da lógica de funcionamento,
a explicação está no arquivo LogicaDefuncionamento.pdf. Leia também o arquivo ReadMe.md para
compreender como executar o código.

"""
import Base
import MultipleWords
import ServiceWords
import PositionBonus


def exec_code(modes):
    if modes == 1:
        while 1:
            input_letters = input("Digite as letras disponíveis nesta jogada: ")
            data = Base.base(input_letters)

            if 'best_word' in data.keys():
                print(f"\n{data['best_word']}, palavra de {data['score']} pontos")
                if data['not_used_letter']:
                    print(f"Sobraram {ServiceWords.format_not_used_letters(data['not_used_letter'])}")
            else:
                print(data['message'])
                print(f"Sobraram {ServiceWords.format_not_used_letters(ServiceWords.treat_letter(input_letters).upper())}")

    elif modes == 2:
        while 1:
            input_letters = input("Digite as letras disponíveis nesta jogada: ")
            data = MultipleWords.multiple_words(ServiceWords.treat_letter(input_letters.lower()))
            ServiceWords.format_output(data)
    elif modes == 3:
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
                print("A posição escolhida é maior do que o tamanho da palavra")
    else:
        print("Essa não é uma opção válida. São válidas apenas as opções 1, 2 e 3.")


try:
    mode = int(input('Digite o modo de funcionamento: '))
    exec_code(mode)
except ValueError:
    print("O modo de funcionamento só aceita valores inteiros")
    exit(0)
