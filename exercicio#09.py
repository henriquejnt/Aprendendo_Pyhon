'''Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e
 mostre a temperatura em graus Celsius'''

fahrenheit = float(input('Graus fahrenheit: '))
conversor_celsius = (fahrenheit - 32) / 1.8
conversor_fahrenheit = fahrenheit * 1.8 + 32 
print(f"{fahrenheit} fahrenheit é equivalente a {conversor_celsius} graus celsius.")