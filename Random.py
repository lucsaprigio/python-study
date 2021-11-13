# Valores aleatórios com random
import random

# Gera um valor de 0.0 a 1.0
print(random.random())

# Gera um valor decimal de Valor mínimo ao Valor Máximo
print(random.uniform(4, 10))

# Gera um valor inteiro de Valor Mínimo ao Valor Máximo
print(random.randint(4, 10))

# Escolher opção aleatória
cores = ['verde', 'vermelhor', 'azul']
print(random.choices(cores, k=2)) # com o k=2, podemos passar dois valores

# Embaralhar valores, passa os 4 valores mas troca as posições
cartas_de_um_baralho = ['carta1', 'carta2', 'carta3', 'carta4'] # Embaralhar
print(random.shuffle(cartas_de_um_baralho))
print(cartas_de_um_baralho)

''' Simulador de Cara ou Coroa'''
lista = ['cara', 'coroa']
print(random.choices(lista))

''' Sorteio entre 5 nomes em uma lista de nomes '''
nomes = ['nome1', 'nome2', 'nome3', 'nome4', 'nome5']
print(random.choice(nomes))

''' Escolher um número aleatório de 10-100'''
print(random.randint(10, 100))