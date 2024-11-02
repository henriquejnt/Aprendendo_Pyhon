#Faça um Programa que pergunte quanto você ganha por hora e o número de horas 
#trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, 
#sabendo-se que são descontados 11% para o Imposto de Renda, 
#8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido

ganha_hora = float(input('Quanto você ganha por hora: '))
horas_por_mes = int(input('Quantas horas trabalha por mês: '))
salario_bruto = horas_por_mes * ganha_hora

#porcentagens feitas para o salario líquido
onze_porcento_salario = (11 / 100) * salario_bruto
oito_porcento_salario = (8 / 100) * salario_bruto
cinto_porcento_salario = (5 / 100) * salario_bruto

#quanto que as deduções legais irá pegar do salario bruto
imposto_renda =  onze_porcento_salario
inss =  oito_porcento_salario
sindicato = cinto_porcento_salario

#soma o total que as deduções ira pegar
soma_deduções = imposto_renda + inss + sindicato

#salario liquido
salario_liquido = salario_bruto - soma_deduções

print('='*25)
print(f"Seu salário bruto é de R${salario_bruto:.2f} reais")
print(f"Você pagou ao INSS R$ {inss:.2f} reais.")
print(f"Você pagou ao SINDICATO R$ {sindicato:.2f} reais.")
print(f"Você pagou ao IMPOSTO DE RENDA R$ {imposto_renda:.2f} reais.")
print(f"Isso totalizou R${soma_deduções} reais de desconto")
print(f"Desse modo, seu salário líquido é de R$ {salario_liquido} reais")