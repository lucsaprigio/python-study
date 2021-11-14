""" 
def nome_da_funcao(parametros):
    comandos:
 """

def dar_boas_vindas():
     print('Bem-vindo!')

dar_boas_vindas()

# Passando Parãmetros
def dar_boas_vindas_personalizado(nome):
    print(f'Bem-vindo(a) {nome}')

dar_boas_vindas_personalizado('Lucas')

# Valor padrão
def apresentar_lugar(lugar='nossa loja'): # Posso passar qualquer tipo de valor
    print(f'Conheça {lugar}')

apresentar_lugar()

""" Desafio 1
    Crie uma função chamada gerar_nome_completo que recebe como 
    parâmetro o nome e sobrenome de alguem e dá boas vindas para essa pessoa
 """

def gerar_nome_completo(nome, sobrenome):
    print(f'Bem-vindo(a) {nome} {sobrenome}')

gerar_nome_completo('Lucas', 'Aprigio')

""" 
    Desafio 2
    Crie uma função chamada calcular_valores
    que recebe 2 parâmetros o primeiro o preco de um produto
    e o segundo parâmetro é a quantidade, porém a quantidade deve haver
    um valor padrão de 1. Sua função deve exibir o resultado do preço
    do produto, multiplicado a quantidade escolhida.
 """

def calcular_valores(preco, quantidade=1):
    print(preco*quantidade)

calcular_valores(10 * 5)