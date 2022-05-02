'''
Variaveis
'''

nome = 'Nícolas da Mota'  #str
idade = 21  #int
altura = 1.88  #float
e_maior = idade > 18  #bool
data_atual = '9 de Abril'
peso = 74
 
print('Nome: ', nome)
print('Idade: ', idade)
print('Altura: ', altura)
print('É maior de idade? ', e_maior)
print('Data: ', data_atual)


# Tarefa
imc = peso / (altura ** 2)

print(nome, 'tem', idade, 'de idade, e seu imc é de: ', imc)