'''Faça um Programa que pergunte quanto você ganha por hora
 e o número de horas trabalhadas no mês. Calcule 
e mostre o total do seu salário no referido mês '''

ganha_por_hora = float(input('Quanto você ganha por hora: '))
horas_por_mes = float(input('Quantas horas você trabalha por mês: '))
salario = horas_por_mes * ganha_por_hora
print(f"No mês você ganha R${salario:.2f} reais")