print('{:=^40}'.format('LOJAS MEL'))
preço = float(input(' Preço das Compras: R$ '))
print(''' FORMAS DE PAGAMENTO
[1] à vista diheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão ''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    total =  preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total =  preço
    parcela = total / 2
    print(' Sua compra será parcelada em 2x de R${:.2f} Sem Juros'.format(parcela))

    
    print('aguarde ...', 'conectando TEF')

elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('Quantas Parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${:.2f} Com juros'.format(totparc, parcela))

    
    print('aguarde ...', 'conectando TEF')

else:
    total = preço
    print('Opção Inválida de pagamento.Tente novamente!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço,  total))


print('aguarde ...', 'conectando TEF')

