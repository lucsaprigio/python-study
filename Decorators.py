from datetime import datetime

# Decorators
def meu_decorator(funcao):
    def wrapper():
        print('Antes')
        funcao()
        print('Depois')
    return wrapper # Passamos a referência, não a função!

@meu_decorator # Quando colocamos esse decorator, não precisamos armazenar na variável abaixo, somente passar a função
def parabenizar():
    print('Parabéns!!!')

# Forma sem decorator
""" resultado = meu_decorator(parabenizar)
resultado() """ 

# Forma com decorator
parabenizar()

"""  Crie um decorator que irá pegar a função que for passado para ele
    e imprimir o horário atual antes de executar a função e depois imprimir
    o horário após ter finalizado a execução da função.
"""

def monitorar_horario(funcao): # ele espera um argumento (funcao) !
    def monitor():
        print(datetime.now())
        funcao() 
        print(datetime.now())
    return monitor # Retorno da função inteira

@monitorar_horario # Nosso decorator, então nao vou precisar passar variável
def baixar_musicas():
    print('Baixando músicas')

baixar_musicas()