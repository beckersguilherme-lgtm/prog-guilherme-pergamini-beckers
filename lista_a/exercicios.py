"""Lista A - Python, listas, busca e custo.

NAO mude o nome deste arquivo nem a assinatura das funcoes.
Escreva sua solucao no lugar do 'pass'.

Os exercicios do Bloco 3 devolvem DOIS valores: o resultado e a contagem.
"""

# ---------- Bloco 1: listas e percurso ----------

def conta_negativos(lista):
    quantidade = 0

    for numero in lista:
        if numero < 0:
            quantidade = quantidade + 1cd

    return quantidade


def media(lista):
    if len(lista) == 0:
        return 0

    soma = 0

    for numero in lista:
        soma = soma + numero

    return soma / len(lista)


def sem_o_maior(lista):
    if len(lista) == 0:
        return []

    nova_lista = lista.copy()
    maior = max(nova_lista)
    nova_lista.remove(maior)

    return nova_lista


def acumulada(lista):
    nova_lista = []
    soma = 0

    for numero in lista:
        soma = soma + numero
        nova_lista.append(soma)

    return nova_lista


def achata(lista_de_listas):
    nova_lista = []

    for lista in lista_de_listas:
        for numero in lista:
            nova_lista.append(numero)

    return nova_lista


# ---------- Bloco 2: busca ----------

def busca_ultima(lista, alvo):
    posicao = -1

    for i in range(len(lista)):
        if lista[i] == alvo:
            posicao = i

    return posicao


def conta_ocorrencias(lista, alvo):
    quantidade = 0

    for numero in lista:
        if numero == alvo:
            quantidade = quantidade + 1

    return quantidade


def primeiro_maior_que(lista, limite):
    for i in range(len(lista)):
        if lista[i] > limite:
            return i

    return -1


def busca_binaria_primeira(lista, alvo):
    inicio = 0
          fim = len(lista) - 1
posicao = -1
 while inicio <= fim:
          meio = (inicio + fim) // 2

        if lista[meio] == alvo:
posicao = meio
     fim = meio - 1

elif lista[meio] < alvo:
                   inicio = meio + 1

        else:
     fim = meio - 1

           return posicao


# ---------- Bloco 3: custo ----------

def soma_pares_contando(lista):
    soma = 0
          operacoes = 0

for numero in lista:
            operacoes = operacoes + 1

        if numero % 2 == 0:
  soma = soma + numero

    return soma, operacoes


def maior_contando(lista):
         maior = lista[0]
    comparacoes = 0

for i in range(1, len(lista)):
             comparacoes = comparacoes + 1

 if lista[i] > maior:
            maior = lista[i]

    return maior, comparacoes


def tem_soma_contando(lista, alvo):
    comparacoes = 0

    for i in range(len(lista)):
for j in range(i + 1, len(lista)):
              comparacoes = comparacoes + 1

if lista[i] + lista[j] == alvo:
         return True, comparacoes

    return False, comparacoes


def ordenada_contando(lista):
    comparacoes = 0

    for i in range(len(lista) - 1):
        comparacoes = comparacoes + 1

        if lista[i] > lista[i + 1]:
            return False, comparacoes

    return True, comparacoes


# ---------- Bloco 4: padroes ----------

def inverte_no_lugar(lista):
    inicio = 0
    fim = len(lista) - 1

    while inicio < fim:
        auxiliar = lista[inicio]
        lista[inicio] = lista[fim]
        lista[fim] = auxiliar

        inicio = inicio + 1
        fim = fim - 1


def eh_palindromo(lista):
    inicio = 0
    fim = len(lista) - 1

    while inicio < fim:
        if lista[inicio] != lista[fim]:
            return False

        inicio = inicio + 1
        fim = fim - 1

    return True


def par_que_soma(lista, alvo):
    inicio = 0
    fim = len(lista) - 1

    while inicio < fim:
        soma = lista[inicio] + lista[fim]

        if soma == alvo:
            return inicio, fim

        elif soma < alvo:
            inicio = inicio + 1

        else:
            fim = fim - 1

    return -1, -1


def soma_maxima_janela(lista, k):
    if k <= 0 or k > len(lista):
        return 0

    soma = 0

    for i in range(k):
        soma = soma + lista[i]

    maior = soma

    for i in range(k, len(lista)):
        soma = soma - lista[i - k]
        soma = soma + lista[i]

        if soma > maior:
            maior = soma

    return maior


def parenteses_balanceados(texto):
    pilha = []

    for caractere in texto:
        if caractere == "(" or caractere == "[":
            pilha.append(caractere)

        elif caractere == ")":
            if len(pilha) == 0:
                return False

            if pilha[-1] != "(":
                return False

            pilha.pop()

        elif caractere == "]":
            if len(pilha) == 0:
                return False

            if pilha[-1] != "[":
                return False

            pilha.pop()

    if len(pilha) == 0:
        return True
    else:
        return False