# Processar VS Retornar
print('Olá!') # Apenas Processa

# Funções que retornam dados
cidade = input('Qual é a sua cidade?')

# Como escolher entre funções que processam VS retornam dados?
""" 
    Eu vou precisar de usar essa informação na lógica do meu programa
    ainda? Ou só preciso processar esse dado, mas não irei utilizar
    mais ele depois?
 """

def exibir_cotacao_do_dia(moeda):
     if moeda == 'usd':
         print(5.47)

exibir_cotacao_do_dia('usd')

# Se eu precisar de uma informação, que será processada dentro da função, nós usamos o return

def obter_cotacao_do_dia(moeda):
    if moeda == 'usd':
        return 5.47

cotacao = obter_cotacao_do_dia('usd')
if cotacao > 5:
    print('Investir em ações americanas')
else:
    print('Cotação não favorável')