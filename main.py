import sys


# INSIRA ABAIXO OS NOMES DOS ALUNOS DO GRUPO (máximo 5 alunos)
# ALUNO 1:
# ALUNO 2:
# ALUNO 3:
# ALUNO 4:
# ALUNO 5:


'''
Escreva uma função com o nome pertence, que recebe como argumentos de
entrada uma tupla e dois itens e retorna True, se os dois itens estiverem
armazenado na tupla, e False, caso contrário.
'''


def pertence(tupla, item1, item2):
    if item1 in tupla and item2 in tupla:
        return True
    return False


'''
Escreva uma função chamada substituir que recebe como argumentos de entrada uma
lista e dois itens (velho e novo) e retorna uma lista onde todas as ocorrências
do item velho são substituídas pelo item novo.
'''


def substituir(lista, velho, novo):
    for elem in lista:
        if elem == velho:
            lista[elem - 1] = novo


'''
Escreva uma função chamada posicoes_lista que recebe como argumentos de
entrada uma lista e um item, e retorna uma tupla contendo todas os índices
em que o item aparece na lista.
'''


def posicoes_lista(lista, item):
    """
    :param indexes -> Lista para armazenar os indeces e retornar
    no final ela em tupla.
    :param cont -> Contador para especificar para a função index
    por onde começar na lista passada como paramêtro.
    index(element, start, end) --> start = cont
    """
    indexes = []
    cont = 0
    for elem in lista:
        if elem == item:
            indexes.append(lista.index(elem, cont))
        cont += 1
    return tuple(indexes)


'''
Suponha um dicionário onde a chave é o nome de um aluno e o valor uma lista
de notas. Escreva uma função chamada reprovados que recebe como argumento de
entrada um dicionário e retorna uma lista com o nome dos alunos reprovados
(um aluno é reprovado quando a média das suas notas é inferior a 6).
'''


def reprovados(alunos):
    alunos_reprovados = []
    for key, value in alunos.items():
        if value < 6:
            alunos_reprovados.append(key)
    return alunos_reprovados


'''
Suponha um dicionário onde a chave é o nome de um aluno e o valor uma lista de
notas. Escreva uma função chamada incluir_nota que recebe como argumentos de
entrada o dicionário, o nome de um aluno e uma nota. A função deve inserir a
nota na lista de notas do aluno correspondente e retornar o dicionário com as
alterações realizadas.
'''


def incluir_nota(alunos, nome, notas):
    """
    incluir_nota({"josé": 5, "Marcio": 3}, 'ronaldo', [1, 2, 3])
    -->> {'josé': 5, 'Marcio': 6, 'ronaldo': [1, 2, 3]} <<--
    """
    alunos[nome] = notas
    return alunos


'''
Suponha um dicionário onde a chave é o nome de um aluno e o valor uma lista
de notas. Escreva uma função chamada menores_notas que recebe como
argumentos de entrada o dicionário e retorna outro dicionário com a
menor nota de cada aluno.
'''


def menores_notas(alunos):
    # sys.maxsize -->> maior valor possível.
    menor_nota = sys.maxsize
    alunos_menores_notas = dict()
    for aluno, notas in alunos.items():
        # Se o valor for multiplo:
        if type(notas) is list:
            for nota in notas:
                if nota < menor_nota:
                    menor_nota = nota
            alunos_menores_notas[aluno] = menor_nota
        # Se o valor for unico:
        else:
            alunos_menores_notas[aluno] = notas
    return alunos_menores_notas


if __name__ == '__main__':
    print("Hello World!")

