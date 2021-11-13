# continue, ignorar/pular
for numero in range(100): # Enquanto o resto for 2 imprima
    if numero % 2 == 0: 
        print(numero)
    else:
        continue # vai ignorar a a condição, e vai contunar

# break, para interromper a interação
for numero in range(100):
    if numero % 2 == 0: 
        print(numero)
    else:
        break # Vai parar a aplicação ja na segunda vez que for falsa