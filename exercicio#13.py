'''Tendo como dado de entrada a altura (h) de uma pessoa, 
construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7'''

h = float(input('Digite sua altura: '))
m_f = str(input('Você é do sexo masculino ou feminino? [m/f]:')).lower
if m_f == 'm':
    formula_m = (72.7*h) - 58
    print(f'Seu peso ideal para o sexo masculino é {formula_m}')
else:
    formula_f = (62.1*h) - 44.7
    print(f'Seu peso ideal para o sexo feminino é {formula_f}')
