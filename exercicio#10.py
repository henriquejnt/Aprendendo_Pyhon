'''Faça um Programa que peça a temperatura em graus Celsius, 
transforme e mostre em graus Fahrenheit.
'''
graus_celsius = float(input('Graus Celsius: '))
converter_fahrenheit = graus_celsius * 1.8 + 32
print(f"{graus_celsius} graus celsius é equivalente a {converter_fahrenheit} graus fahrenheit")