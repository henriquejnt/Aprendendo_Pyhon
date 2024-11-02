#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em 
#metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de
#1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
#que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas
#e o preço total.

tamanho = float(input('Digite o tamanho da área: '))
quantidade_litros_pintura = tamanho / 3.0
quantidade_latas = quantidade_litros_pintura / 18.00
valor_latas = quantidade_litros_pintura * 80.00
print(f'Para a área de {tamanho:.1f} metros será necessario {quantidade_latas:.1f} latas de tintas')
print(f"Desse modo, será necessario R${valor_latas:.2f} reais para realizar essa pintura.")