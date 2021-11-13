#Criando um Laço de Repetição

# numero é o nome do laço, o range faz percorre o indice, então nao vai contar o 0,
# O 2 será o segundo parâmetro, que vai contar de 2 em 2.
for numero in range(1, 21, 2):
    print('carregando', numero)

# Os nomes nós que escolehmos, a Variável Nome abaixo, armazena um indice de Nomes
# o "nome" depois do for, é o nome do Loop, e o in, é o índice que queremos percorrer.
nomes = ['Jeff', 'Carl', 'Jean', 'Luke']
for nome in nomes:
    print(nome)


# Usando um loop, exiba na tela: Estamos em X onde x éum valor iniciando 18 e finalizando em 110
for x in range(18, 111):
    print(x)

# Você precisa de 10 passos para finalizar uma tarefa, exiba na tela, usando loop for a seguinte frase
# "Realizando passo X"

for passo in range(1, 11):
    print(f'Realizando passo {passo}')