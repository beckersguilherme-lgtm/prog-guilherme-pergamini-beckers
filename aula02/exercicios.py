"""Aula 02 - Listas em Python.

NAO mude o nome deste arquivo nem a assinatura das funcoes.
Escreva sua solucao no lugar do 'pass'.
"""


def remove_negativos(lista):
    """Devolve uma lista nova só com os números que não são negativos."""
    return [x for x in lista if x >= 0]


def inverte(lista):
    """Devolve uma lista nova na ordem contrária.
    Sem usar reverse() e sem usar [::-1]."""
    nova_lista = []
    for i in range(len(lista) - 1, -1, -1):
        nova_lista.append(lista[i])
    return nova_lista


def busca_binaria(lista, alvo):
    """Recebe uma lista JÁ ORDENADA. Devolve a posição do alvo, ou -1."""
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1

    return -1


def intercala(lista_a, lista_b):
    """Devolve uma lista nova alternando os elementos das duas.
    As duas listas têm o mesmo tamanho."""
    resultado = []
    for i in range(len(lista_a)):
        resultado.append(lista_a[i])
        resultado.append(lista_b[i])
    return resultado


def remove_repetidos(lista):
    """Devolve uma lista nova sem elementos duplicados, mantendo a ordem original."""
    nova_lista = []
    for elemento in lista:
        if elemento not in nova_lista:
            nova_lista.append(elemento)
    return nova_lista