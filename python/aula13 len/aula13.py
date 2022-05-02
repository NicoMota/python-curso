''''
Contar caracteres
Funcão Len
'''

usuario = input('Digite set user: ')
qnt_caract = len(usuario)

#print(f'Seu usuário é {usuario}, com a quantidade de {qnt_caract} caracteres')
#print(usuario, qtd_carac, type(usuario))

if qnt_caract > 5 and qnt_caract < 10:
    print(f'Usuário cadastrado, seu usúario tem {qnt_caract} caracteres')
else:
    print('Erro')


str1 = input('Digite uma coisa: ')
str2 = input('Digite outra coisa: ')

#print(f'A quantidade de caracteres das frases são {len(str1 + str2)}')
print(f'A quantidade de caracteres das frases são {len(str1)  + len(str2)}')


