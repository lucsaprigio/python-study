# Laço While

# Vamos imaginar um número de tentativas de escrever uma senha
tentativas = 0
while tentativas < 3: # Enquanto essa condição for verdadeira
    print('Senha Incorreta, Tente novamente!') # Rode isso
    tentativas += 1 # E Incrementa um valor

# Trataviva de Senha,
# Conseguimos travar o usuário em uma tela de login e senha
# Enquanto a senha não for exatamente igual a Condição, então Volte no input novmente
# Caso o contrário, printa Bem-Vindo
senha = ''
while senha != '123456': 
    senha = input('Digite sua senha: ')
    print('Senha Incorreta!')
print('Bem-vindo!')

# Receber nome do usuário
nome = ''
while nome == '':
    nome = input('Digite seu nome: ')
    print('Por favor, digite seu nome.')
print(f'Bem vindo {nome}') # Enquanto as condições acima forem falsas, não sai do loop

# Ver por do sol as 17:00
horario = 0
while horario <= 17:
    print(horario)
    horario += 1
print('Hora de ir ver o por do sol')

contador = 100
while contador >= 0:
    print(contador)
    contador -= 1

# Desafio 1 - Crie um loop while que irá contar e imprimir no console de 1 até 120
contador = 1
while contador < 121:
    print(contador)
    contador += 1

""" Desafio 2 - Cria um loop while que irá continuamente pedir ao usuário
 a senha para entrada, e só irá permitir o programa continuar caso ele digite
 a senha 'secreto' """
senha = ''
while senha != 'secreto': # Enquanto a senha for DIFERENTE de secreto, continue a baixo
    senha = input('Digite sua senha: ')

""" Desafio 3 - Crie um loop que conte em ordem descrescente de 100 para 1"""
contador = 100
while contador > 0:
    print(contador)
    contador -= 1