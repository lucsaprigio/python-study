from datetime import datetime

# Pega a data atual
print(datetime.now())

# Passando a propriedade abaixo, pega o Dia, Mês ou ano
print(datetime.now().day)
print(datetime.now().month)
print(datetime.now().year)

# Criar uma data
lancamento_app = datetime(2021, 5, 28)
print(lancamento_app)
# Quero receber a data lançamento do meu aplicativo
data_de_lancamento =datetime.strptime(input('Quando devemos lançar o aplicativo?'), '%d/%m/%Y')
print(type(data_de_lancamento))

# Calcular o intervalo entre datas
data_atual = datetime.now()
prazo = data_de_lancamento - data_atual
print(prazo.days)

#DESAFIO
# Calcule quantos dias faltam até o seu aniversário

atual_data = datetime.now()
aniversario = datetime.strptime(input('Digite a Data do seu aniversário'), '%d/%m/%Y')
dias = aniversario - atual_data
print(dias.days)
