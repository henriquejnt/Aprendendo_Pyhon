maior = 0
menor = 0
for j in range(1, 6):
    peso = float(input('Peso da {} pessoa: '.format(j)))
    if j ==1:
       maior = peso
       menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido é {}kg '.format(maior))
print('e o menor peso lido é {}kg '.format(menor))