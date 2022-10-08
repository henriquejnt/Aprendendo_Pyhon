# Programa que leia um número e diz se é ou não um número primo.

primo = int(input('Digite um número qualquer: '))
l = 0
for j in range(1, primo + 1):
    if primo % j == 0:
        print('\033[34m', end='')
        l = l + 1
    else:
        print('\033[37m', end='')
    print("{} ".format(j), end='')
print('\n\033[mO número {} foi dividido por {} vezes.'.format(primo, l))
if l == 2:
    print('Por isso ELE É PRIMO.')
else:
    print('Por isso ELE NÃO É PRIMO.')
