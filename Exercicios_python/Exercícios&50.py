# programa de 6 números inteiros que mostra a soma apenas dos números pares;
# E que ignora os números impares.

soma = 0
count = 0
for j in range(1, 7):
    n1 = int(input('Digite o {} valor: '.format(j)))
    if n1 % 2 ==0:
     soma = soma + n1
     count = count + 1
print('Voce digitou {} números pares e a soma é {}'.format(count, soma))