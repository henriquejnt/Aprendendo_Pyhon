print('Calculo do IMC')
peso = int(input('Qual o seu peso ? '))
altura = float(input('Qual a sua altura ? '))
print('\033[34;1m CALCULANDO O SEU IMC ....\033[m')
imc = peso / (altura * altura)
if imc <= 18.5:
    print('O IMC dessa pessoa  é {:.1f}'.format(imc))
    print("\033[31;1mVoce esta com ABAIXO DO PESO !!\033[m")
elif 18.5 <= imc < 25:
    print('O IMC dessa pessoa  é {:.1f}'.format(imc))
    print('\033[1m Voce esta com o PESO IDEAL .')
elif 25 <= imc < 30:
    print('O IMC dessa pessoa  é {:.1f}'.format(imc))
    print('\033[1m Voce esta com SOBRE PESO !')
elif 30 <= imc < 40:
    print('O IMC dessa pessoa  é {:.1f}'.format(imc))
    print('\033[31;1 m Voce esta com OBESIDADE !!!')
elif imc >= 40:
    print('O IMC dessa pessoa  é {:.1f}'.format(imc))
    print('\033[31;1m Voce esta com OBESIDADE MÓRBIDA ,cuidado !!!\033[m')
