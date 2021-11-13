# Loops Aninhados
# Pais + Estação

# Loop dentro de outro Loop

paises = ['brasil', 'india', 'estados unidos']
estacoes_do_ano = ['primavera', 'verão', 'outono', 'inverno']
for pais in paises:
    for estacao in estacoes_do_ano:
        print(f'{pais} {estacao}')

# Imprima na tela a marca + celular de todos celulares, usando informações abaixo
celulares = ['Asus', 'Samsung', 'Sony', 'IPhone']
versoes = ['Plus', 'Premium Plus', 'Premium Deluxe', 'Plus Primium Ultra']

for celular in celulares:
    for versao in versoes:
        print(f'{celular} {versao}')