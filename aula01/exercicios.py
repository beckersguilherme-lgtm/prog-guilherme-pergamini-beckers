"""Aula 01 - De C para Python.

NAO mude o nome deste arquivo nem a assinatura das funcoes.
Escreva sua solucao no lugar do 'pass'.
"""


def soma_lista(lista):
    """Devolve a soma de todos os numeros da lista. Lista vazia devolve 0."""
    
    def soma_lista(lista):
    total = 0
    for num in lista:
        total += num
    return total


def conta_pares(lista):
    """Devolve quantos numeros da lista sao pares."""

    def conta_pares(lista):
    qtd = 0
    for num in lista:
        if num % 2 == 0:
            qtd += 1
    return qtd


def maior_valor(lista):
    """Devolve o maior numero da lista. A lista nao esta vazia."""
    
    def maior_valor(lista):
    maior = lista[0]
    for num in lista:
        if num > maior:
            maior = num
    return maior


def existe(lista, alvo):
    """Devolve True se o alvo esta na lista, False se nao esta."""
    
    def existe(lista, alvo):
    for num in lista:
        if num == alvo:
            return True
    return False


def busca_linear(lista, alvo):
    """Devolve a posicao do alvo na lista, ou -1 se ele nao estiver."""
    
    def busca_linear(lista, alvo):
    for i in range(len(lista)):
        if lista[i] == alvo:
            return i
    return -1


def segundo_maior(lista):
    """(Desafio) Devolve o segundo maior, percorrendo a lista uma unica vez."""
    
    def segundo_maior(lista):
    maior = float('-inf')
    segundo = float('-inf')
    
    for num in lista:
        if num > maior:
            segundo = maior
            maior = num
        elif num > segundo:
            segundo = num
            
    return segundo
