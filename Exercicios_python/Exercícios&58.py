'''o computador vai pensar no numero de 0 a 10 ,mas o usuario vai tentar ate acertar
,Mostrando no final os palpites que usou ate acertar'''

from  random import randint
b = randint(0,10)
print('\033[1m Tenta acertar o número que o COMPUTADOR esta pensando!\033[m')
ACERTOU = False
PALPITES = 0
while not ACERTOU:
    n = int(input('\033[31:1m Tente adivinhar o Número: \033[m'))
    PALPITES = PALPITES + 1
    if n == b:
        ACERTOU = True
print('\033[32:1m voce acertou,O COMPUTADOR pensou no número {} e o numero de tentativas foi {} . \033[m'.format(b,PALPITES))