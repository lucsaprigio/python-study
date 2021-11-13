# Vamos pensar por exemplo no seguinte:
idade = 21
possui_convite = False
filho_do_dono = True
print(idade >= 21 and possui_convite == True)
print(idade >= 21 or possui_convite == True)
# maior de 21 e possui convite ou seja filho do dono
print((idade > 21 and possui_convite == True) or 
(filho_do_dono == True))

maior_de_idade = True
possui_carteira_de_trabalho = True
trabalha_atualmente = True
possui_veiculo_proprio = False

# Você só pode trabalhar aqui se for maior de idade E possuir carteira de trabalho
print((maior_de_idade == True) and (possui_carteira_de_trabalho == True))

# Queremos contratar pessoas que ainda NÃO(and not) possuem um veículo próprio, mas já possuam carteira de trabalho
print((possui_carteira_de_trabalho == True) and not possui_veiculo_proprio)

# Desafio
possui_passaporte = True
passagem_comprada = True
menor_de_idade = False

print((possui_passaporte == True) and (passagem_comprada == True and not menor_de_idade))
print((possui_passaporte == True) or (passagem_comprada == True) and not (menor_de_idade))
print(not possui_passaporte or (passagem_comprada) and not (menor_de_idade))
