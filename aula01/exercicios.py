def soma_lista(lista):
    """Devolve a soma de todos os numeros da lista. Lista vazia devolve 0."""
    total = 0
    for num in lista:
        total += num
    return total


def conta_pares(lista):
    """Devolve quantos numeros da lista sao pares."""
    qtd = 0
    for num in lista:
        if num % 2 == 0:
            qtd += 1
    return qtd


def maior_valor(lista):
    """Devolve o maior numero da lista. A lista nao esta vazia."""
    maior = lista[0]
    for num in lista:
        if num > maior:
            maior = num
    return maior


def existe(lista, alvo):
    """Devolve True se o alvo esta na lista, False se nao esta."""
    for num in lista:
        if num == alvo:
            return True
    return False


def busca_linear(lista, alvo):
    """Devolve a posicao do alvo na lista, ou -1 se ele nao estiver."""
    for i in range(len(lista)):
        if lista[i] == alvo:
            return i
    return -1


def segundo_maior(lista):
    """(Desafio) Devolve o segundo maior, percorrendo a lista uma unica vez."""
    maior = float('-inf')
    segundo = float('-inf')

    for num in lista:
        if num > maior:
            segundo = maior
            maior = num
        elif num >= segundo:
            segundo = num

    return segundo