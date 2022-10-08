''' LER O SEXO DE UMA PESSOA ,MAS SO ACEITAR OS VALORES M e F
 se tiver errado,peça a digitação novamente.'''

s = str(input('Qual o seu sexo? [F/M] ')).strip().upper()[0]
while s not in 'MmFf':
    s = str(input('Dados inválidos.Por favor informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(s))