nome = input('Digite seu nome completo: ')
nome = nome.upper()

lista = list(nome)
lista.reverse()

print(''.join(lista))
