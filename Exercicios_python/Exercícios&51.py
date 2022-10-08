
# Programa que mostra o primeiro termo e razão de uma P.A e no final mostra os 10 primeiros termos.


t1 = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
D = t1 + (10 - 1) * razao
for j in range(t1, D + razao, razao):
    print(j, end=' -> ')
print('ACABOU!!')