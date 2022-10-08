''''LER 2 VALORESE E DPS MOSTRA UM MENU Q É PRA 1SOMAR,2MULIPLICAR,3 MAIOR NUMERO,4 NOVOS
NUMEROS E 5SAIR.O PROGRAMA DEVERÁ REALIZAR O PROGRAMA EM CADA CASO'''

n1 =int(input('Digita um número:'))
n2 =int(input('Digita outro número: '))
menu = 0
while menu !=5 :
    print('''[1] soma
    [2] multiplicação
    [3] maior 
    [4] novos numeros
    [5] sair''')
    op = int(input('Qual opção você escolhe? '))
    if op ==1:
       soma= n1 + n2
       print('A soma é {}'.format( soma))
    elif op ==2:
        multi = n1 * n2
        print('A multiplição é {}'.format(multi))
    elif op ==3:
        m = max(n1,n2)
        print('O maior número é {}'.format(m))
    elif op ==4:
        n1 = int(input('Digita um número:'))
        n2 = int(input('Digita outro número: '))
    elif op ==5:
        print('VOCÊ SAIU DO PROGRAMA...')
    else :
        print('DÁDOS INVÁLIDOS,tente novamente!!!')



