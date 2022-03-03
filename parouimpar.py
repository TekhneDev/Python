"""
Fazer um programa que peça ao usuario para digitar um numero inteiro, informe se este numero é par ou impar.
Caso o usuario nao digite um numero inteiro, informe que nao é um numero inteiro.
"""
#FAZENDO AO CONTRARIO
numero_inteiro = input('Digite um número inteiro: ')

if not numero_inteiro.isdigit():
    print('Isso não é um número inteiro.')
else:
    numero_inteiro = int(numero_inteiro)
    if not numero_inteiro % 2 == 0:
        print(f'{numero_inteiro} é Ímpar.')
    else:
        print(f'{numero_inteiro} é Par.')
