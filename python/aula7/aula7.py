nome = 'Nícolas da Mota'  # str
idade = 21  # int
altura = 1.88  # float
e_maior = idade > 18  # bool
data_atual = '9 de Abril'
peso = 74
imc = peso / (altura ** 2)

print(nome, 'tem', idade, 'anos de idade e seu imc é de: ',imc)
print(f'{nome} tem {idade} anos de idade e seu imc é de {imc:.2f}')
print('{} tem {} anos de idade e seu imc é de {:.2f}'.format(nome, idade, imc))
