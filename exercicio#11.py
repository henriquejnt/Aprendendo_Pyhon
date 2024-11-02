'''Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.'''

n1 = int(input('Primeiro número inteiro: '))
n2 = int(input('Segundo número inteiro: '))
real = float(input('Número real: '))
dobro_primeiro_metade_segundo = (n1*2) * (n2 / 2)
soma_do_triplo_primeiro_terceiro = (n1 * 3) + real 
terceiro_ao_cubo = real ** 3
print('O produto do dobro do primeiro com metade do segundo é {} '.format(dobro_primeiro_metade_segundo))
print('A soma do triplo do primeiro com o terceiro é {}'.format(soma_do_triplo_primeiro_terceiro))
print('O terceiro elevado ao cubo é {}'.format(terceiro_ao_cubo))