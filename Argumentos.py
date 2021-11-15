def exibir_preco(nome_produto, preco):
    print(f'{nome_produto} está no valor de: {preco}')

#Argumentos posicionais
exibir_preco('Iphone', 5000)

# Argumentos nomeados
exibir_preco(nome_produto='Iphone', preco=5000)


""" DESAFIO 1
    Crie uma função chamado gerar_objeto_personalizado que irá
    receber 3 parâmetros, cor, altura, formato. A sua função
    deve imprimir na tela o que foi passado para ela, nada mais, nada
    menos. Porém ela deve seguir as seguintes regras: 
    1 - O primeiro argumento deve ser posicional 2.
    - Os argumentos altura e formato precisam OBRIGATORIAMENTE serem nomeados
 """

# O que vem após o * são obrigatorios.
def gerar_objeto_personalizado(cor, *, altura, formato):
    print (f'{cor}, {altura}, {formato}')

gerar_objeto_personalizado('Vermelho', altura=1.70, formato='Quadrado')


# Argumentos Dinâmicos
def somar(*valores, b):
    print(valores)
    for valor in valores:
        b += valor
    print(b)

somar(10, 20, 5, b=5)

#*args

# **Kwargs(KEyword arguments)
def concatenar(**palavras):
    frase = ''
    for palavra in palavras.values():
        frase += palavra + ' '
    print(frase)

concatenar(a='Nós', b='Somos', c='Pythonistas')


def fazer_calculo(nome, *args, **kwargs):
    print(nome)
    print(args)
    print(kwargs)
    for arg in args:
        print(arg)
    for kwarg in kwargs.values():
        print(kwarg)

fazer_calculo('Jeff',4, 5, 6, 7, 8, a=1, b=2, c=3)
