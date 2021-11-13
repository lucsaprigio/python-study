trabalho_terminado = True
if trabalho_terminado == True: # Caso for True as duas condições cai nessa
    print('Bora dar uma saída!')
else:
    print('Não posso sair agora.') # Se for Falsa, Vai cair nessa

# Caso o número de atrasos for maior ou igual a 3 ele vai para dirtoria
numero_atrasos = 2
if numero_atrasos >= 3: # Se essa condição for verdadeira vai cair no print abaixo
    print('Vá para a diretoria')
elif numero_atrasos == 2: # Se a condição acima for Falsa, vai cair nessa
    print('Essa é sua segunda falta')
elif numero_atrasos == 1: # Caso for falsa cai nessa
    print('Essa é sua primeira falta')
else: # e por último, se todas acima for falsa vai nessa.
    print('Pode entrar')

'''A velocidade máxima para essa rua é 50km
    * Cruzou entre 51km a 60km, levou multa de 2 pontos
    * Cruzou entre 61km a 75km, levou multa de 3 pontos
    * Cruzou acima de 75km, levou multa de 7 pontos
'''

velocidade = 55
if velocidade <= 50:
    print('Não foi multado')
elif velocidade >= 51 and velocidade <= 60:
    print('Levou multa de 2 pontos')
elif velocidade >= 61 and velocidade <= 75:
    print('Levou multa de 3 pontos')
else: 
    print('Levou multa de 7 pontos')

# Desafio
''' Você está montando um sistema para um salão de 
beleza para calcular o preço do corte de cabelos grandes que irá
seguir regras:
    * Se seu cabelo estiver ccom ou abaixo de 20cm você paga o valor de R$50,00
    * Se seu cabelo stiver entre 21cm a 30cm você paga o valor de R$70,00
    * Se seu cabelo tiver entre 31cm a 50cm você paga o valor de R$100,00
    * Acima de 50cm Favor consultar na recepção
'''
tamanho_cabelo = 15
if tamanho_cabelo < 20:
    print('O Valor será de R$50,00!')
elif tamanho_cabelo >= 21 and tamanho_cabelo <= 30:
    print('O valor será de R$70,00!')
elif tamanho_cabelo >= 31 and tamanho_cabelo<= 50:
    print('O valor será de R$100,00')
else:
    print('Favor consultar na recepção')
