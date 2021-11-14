from turtle import Turtle

# Inicializar uma turtle
t = Turtle()

# Definir a velocidade
t.speed(1) # de 1 a 10
while True: # Enquanto for verdadeiro
    direcao = input('Para qual direção devemos ir? "f:frente" ou "t:trás" ')
    if direcao == 'f':
        distancia = int(
            input('Quantos pixels devemos movimentar para a frente? ')
        )
        movimentar_para_lado = input(
            'Rotacionar para d:direita, e:esquerda, n:não rotacionar ')
        if movimentar_para_lado == 'd':
            angulo = int(input('Quanto para direita devemos rotacionar? '))
            t.right(angulo)
        elif movimentar_para_lado == 'e':
            angulo = int(input('Quanto para esquerda devemos rotacionar? '))
            t.left(angulo)
        t.forward(distancia)
    if direcao == 't':
        distancia = int(
            input('Quantos pixels devemos movimentar para trás? '))
        movimentar_para_lado = input(
            'Rotacionar para d: direita, e:esquerda, n:não rotacionar')
        if movimentar_para_lado == 'd':
            angulo = int(input('Quanto para direita devemos rotacionar? '))
            t.right(angulo)
        elif movimentar_para_lado == 'e':
            angulo = int(input('Quanto para esquerda devemos rotacionar ? '))
            t.left(angulo)
        t.backward(distancia)
    resposta = input('Continuar andando?(sim/s) (não/n): ')
    if resposta not in ('sim', 's'):
        break