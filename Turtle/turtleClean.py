from turtle import Turtle

# Inicializar uma turtle
t = Turtle()

# Definir a velocidade
def obter_distancia():
    resposta = int(input('Quantos pixels devemos movimentar para a frente? '))
    return resposta

def rotacionar_turtle(turtle):
            movimentar_para_lado = input(
                'Rotacionar para d:direita, e:esquerda, n:não rotacionar ')
            if movimentar_para_lado == 'd':
                rotacionar_para_direita(turtle)
            elif movimentar_para_lado == 'e':
                rotacionar_para_esquerda(turtle)
def rotacionar_para_direita(turtle):
        angulo = int(input('Quanto para direita devemos rotacionar? '))
        t.right(angulo)

def rotacionar_para_esquerda(turtle):
        angulo = int(input('Quanto para esquerda devemos rotacionar? '))
        t.left(angulo)

t.speed(1) # de 1 a 10
while True: # Enquanto for verdadeiro
    direcao = input('Para qual direção devemos ir? "f:frente" ou "t:trás" ') # Duas opções
    if direcao == 'f': # Se a resposta for F
        distancia = obter_distancia()
        rotacionar_turtle(t)
        t.forward(distancia)
    if direcao == 't':
        distancia = obter_distancia()
        rotacionar_turtle(t)
        t.backward(distancia)
    resposta = input('Continuar andando?(sim/s) (não/n): ') 
    if resposta not in ('sim', 's'): # se não for S ou SIM
        break # Finalize