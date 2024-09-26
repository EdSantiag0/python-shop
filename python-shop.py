print('\033[1;32;40m-==-==-==- LOJA BOM PREÇO -==-==-==-\033[m')
total = valor = soma = quantidade = totquant = item = 0
while True:
    item = str(input('Produto: '))
    valor = float(input('Valor: R$'))
    quantidade = int(input('Quantidade: '))
    soma = valor * quantidade
    total += soma
    totquant += quantidade
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja Continuar? [S/N]')).strip().upper()[0]
        print('='*30)
        if continuar == 'N':
            print('Dados da Compra')
            print(f'{totquant} Produtos no valor Total de: R${total}')
            verificação = ' '
            while verificação not in 'SN':
                verificação = str(input('Deseja Finalizar Pedido? [S/N]')).strip().upper()[0]
    if verificação == 'S':
        break