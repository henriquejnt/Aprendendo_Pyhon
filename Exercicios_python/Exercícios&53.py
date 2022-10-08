# programa que lea uma frase e diz se é ou não UM PALÍNDROMO,desconsiderando os espaços.

frase = input("Qual a frase? ").upper().replace(" ", "")
if frase == frase[::-1]:
    print("A frase é um palíndromo")
else:
    print("A frase não é um palíndromo")