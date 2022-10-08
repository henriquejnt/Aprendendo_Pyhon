media = 0
m = 0
nomevelho = ''
marioridadehomem = 0
menorde20mulher = 0
for p in range(1, 5):
   print('{} PESSOA'.format(p))
   nome = str(input('Nome: ')).strip()
   idade = int(input('Idade: '))
   sexo = str(input('Sexo [M/F]: ')).strip()
   media = idade + media
   if p == 1 and sexo in 'Mm':
      marioridadehomem = idade
      nomevelho = nome
   if sexo in 'Mm' and idade > marioridadehomem:
      marioridadehomem = idade
      nomevelho = nome
   if sexo in 'Ff' and idade < 20:
      menorde20mulher += 1
m = media / 4
print('A média de idade do grupo é de {} anos'.format(m))
print('O homem mais velho tem {} e se chama {} .'.format(marioridadehomem, nomevelho))
print('Tem {} mulheres menores de 20 anos.'.format(menorde20mulher))