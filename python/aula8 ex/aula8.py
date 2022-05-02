'''
Exercio:
Mostrar:
    Luiz tem 32 anos, 1.8 de altura e pesa 80KG
    O IMC de Luiz é igual a: 24.69
    Luiz nasceu em 1990
'''

nome = 'Luiz'
idade = 32
altura = 1.80
peso = 80.5
imc = peso / altura ** 2
ano = 2022
nasc = ano - idade


print(
    f'Luiz tem {idade} anos, {altura} de altura e pesa {peso}KG\n'
    f'O IMC de {nome} é igual a: {imc:.2f}\n'
    f'{nome} nasceu em {nasc}'
)