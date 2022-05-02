"""
Operadores Relacionais
== > >= < <= !=
"""

nome = input('Qual seu nome? ')
idade = input('Qual sua idade? ')

# ilim = input('Qual idade limite para pode ter empréstimo? ')
# elim = int(ilim)

idade = int(idade)

# Limite para empréstimo
menor_idade = 20
maior_idade = 30


if idade >= menor_idade and idade <= maior_idade:
    print(f'{nome} você tem idade para liberar o empréstimo')
else:
    print(f'{nome} você nao tem idade para receber o emprestimo. =( ')