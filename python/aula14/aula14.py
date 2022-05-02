# https://docs.python.org/3/library/stdtypes.html
# https://github.com/luizomf/check-numbers-python/blob/master/chk_numbers.py
import re


def is_float(val):
    if isinstance(val, float): return True
    if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', val): return True

    return False


def is_int(val):
    if isinstance(val, int): return True
    if re.search(r'^\-{,1}[0-9]+$', val): return True

    return False


def is_number(val):
    return is_int(val) or is_float(val)


num1 = input('Digite um número: ')
num2 = input('Digite outro número: ')

if is_number(num1) and is_number(num2):
    num1 = float(num1)
    num2 = float(num2)

    calc = num1 + num2

    print(f'A soma dos numeros é: {calc}')
else:
    print('Digite um número valido')