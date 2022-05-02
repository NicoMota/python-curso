"""
Operadores Lógicos
and, or, not
in e not in
"""

#  Verdadeiro e Falso = Falso
# comparacao1 and comparacao2

# Verdadeiro ou Verdadeiro = Verdadeiro
# comparacao1 or comparacao21


num1 = input('Digite um numero: ')
num2 = input('Digite um numero: ')

if num1 > num2:
    print(f'{num1} é maior que o numero {num2}')
else:
    print(f'{num1} é menor que o numero {num2}')

nome = input('Qual o seu nome? ')

if 'Nico' in nome:
    print('Nico tem em seu nome')
else:
    print('Não tem nico em seu nome')

print('Vamos realizar seu login')

login = input('Usuário: ')
senha = input('Senha: ')

login_dados = 'nicolas'
senha_dados = '123456'

if login == login_dados and senha == senha_dados:
    print('Você está logado')
else:
    print('Usuário ou senha incorreto.')




