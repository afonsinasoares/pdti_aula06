def tamanho_texto(texto1,texto2):
    if len(texto1) == len(texto2):
        print('Tamanhos iguais')
    else:
        print('Tamanhos diferentes')

def possui_mesmo_conteudo(texto1, texto2):
    if texto1.lower() == texto2.lower():
        print('Textos iguais')
    else:
        print('Textos diferentes')

texto1 = input('Informe o texto 1:')
texto2 = input('Informe o texto 2:')

print(texto1,':', len(texto1), 'caracteres')
print(texto2,':', len(texto2), 'caracteres')

tamanho_texto(texto1, texto2)
possui_mesmo_conteudo(texto1, texto2)