def nome_mes(mes):
    numero_mes = int(mes)
    if numero_mes < 1 or numero_mes > 12:
        return 'Mês inválido'
    meses=['Janeiro','Fevereiro','Março',
           'Abril','Maio','Junho','Julho',
           'Agosto','Setembro','Outubro',
           'Novembro','Dezembro']
    return meses[numero_mes - 1]

# resolver depois
# def eh_data_valida(data):
#     return True

data = input('Data de nascimento DD/MM/AAAA: ')

# elementos_da_data = []
# if data.find("-") >= 0:
#     elementos_da_data = data.split('-')
# elif data.find("/") >= 0:
#     elementos_da_data = data.split('/')

elementos_da_data = data.split('/')
print(f'Você nasceu em {elementos_da_data[0]} de {nome_mes(elementos_da_data[1])} de {elementos_da_data[2]}.')