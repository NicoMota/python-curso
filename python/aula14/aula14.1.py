num1 = input('Digite um número: ')
num2 = input('Digite outro número: ')

try:
    num1 = float(num1)
    num2 = float(num2)

    calc = num1 + num2

    print(f'A soma dos numeros é: {calc}')
except:
    print('Digite um número valido')